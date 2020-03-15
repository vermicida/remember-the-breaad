# Remember The Bread

Su nombre está inspirado en el gran [Remember The Milk](https://www.rememberthemilk.com/), pero no te dejes engañar, esto es una _to-do list_ más simple que el mecanismo de un chupete. Es una aplicación [Flask](https://palletsprojects.com/p/flask/) que corre sobre [Gunicorn](https://docs.gunicorn.org/en/stable/), y se apoya en [MySQL](https://www.mysql.com/) para la persistencia de los datos.

## Despliegue en EC2

Esta aplicación se ejecuta en un contenedor [Docker](https://www.docker.com/). El primer paso que debemos hacer, por tanto, es generar la imagen. Podemos hacerlo desde una terminal ejecutando el siguiente comando:

```bash
$ docker build -t rtb .
````

Posteriormente, esta imagen se deberá etiquetar y subir a un repositorio de imágenes que consideremos oportuno y al que la instancia de EC2 tenga acceso para su descarga. La buena noticia es que todo esto ya lo hemos hecho por ti, y tienes la imagen disponible en [Docker Hub](https://hub.docker.com/r/vermicida/rtb) lista para usar.

```bash
$ docker pull vermicida/rtb
```

Lo siguiente que debemos hacer es crear un secreto en [AWS Secrets Manager](https://eu-west-1.console.aws.amazon.com/secretsmanager/home?#/home) para almacenar de forma segura los parámetros de conexión de la base de datos MySQL. Este secreto debe llamarse `rtb-db-secret` y contener las siguientes keys:

- **username:** usuario válido de la base de datos.
- **password:** contraseña del usuario indicado.
- **host:** IP o DNS del servidor donde está levantada la base de datos.
- **db:** nombre de la base de datos.

**Remember The Bread** lee este secreto al iniciarse y genera la cadena de conexión con la base de datos; la instancia de EC2, por tanto, debe tener un rol asociado que le permita realizar esta acción.

Continuamos creando una nueva intancia de EC2 con **Amazon Linux 2** como sistema operativo y, dado lo poco exigente que es esta aplicación en cuanto a recursos, un tipo **t2.micro** será más que suficiente. Es importante asignar a la instancia una **IPv4 pública** y permitir las peticiones **TCP** entrantes en el puerto **8080**. Por último, configuramos el **User Data** con el siguiente script:

```bash
#!/bin/bash
sudo yum update -y
sudo yum install -y docker
sudo service docker start
sudo docker run -d --name rtb -p 8080:8080 vermicida/rtb
```

Este script instalará la paquetería de sistema necesaria y levantará la aplicación en el puerto 8080. Solo queda navegar a la IP pública de la instancia para poder usar **Remember The Bread**.
