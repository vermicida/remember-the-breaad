FROM python:3.6-alpine

RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc libc-dev && \
    apk add --no-cache mariadb-dev

ADD requirements.txt /opt

RUN pip install -r /opt/requirements.txt && \
    rm /opt/requirements.txt && \
    apk del .build-deps

ADD src /opt/src

WORKDIR /opt/src

EXPOSE 8080

ENTRYPOINT [ "python", "wsgi.py" ]
