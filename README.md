# Remember the Bread

## Puesta a punto

Es necesario tener instalada la siguiente paquetería a nivel de sistema operativo:

- python3-devel
- mysql-devel
- gcc

Hacemos uso de **yum** para instalar estos paquetes:

```bash
$ sudo yum update -y
$ sudo yum install -y python3-devel mysql-devel gcc
```

Lo siguiente que debemos hacer es instalar las dependencias a nivel aplicativo. Para ello nos apoyamos en **pip**:

```bash
$ sudo pip3 install -r requirements.txt
```

La configuración de acceso a la base de datos se obtiene de [AWS Secrets Manager](https://eu-west-1.console.aws.amazon.com/secretsmanager/home?#/home). La instancia de EC2 debe tener el IAM Role adecuado para consultar este servicio. Se debe crear un nuevo secreto de nombre `rtb-db-secret` para almacenar los siguientes datos:

- **username:** usuario válido de la base de datos.
- **password:** contraseña del usuario indicado.
- **host:** IP o DNS del servidor donde está levantada la base de datos.
- **db:** nombre de la base de datos.

El tipo de secreto **Credentials for RDS database** nos facilita esta tarea; importante, eso sí, tener en cuenta que requiere edición posterior para añadir **db**, que no lo obtiene de forma automática.
