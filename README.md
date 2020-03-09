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
