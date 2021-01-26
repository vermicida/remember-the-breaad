# OS base image.
FROM python:3.6-alpine AS os-base
RUN apk update && \
    apk add --no-cache --virtual .build-deps gcc g++ musl-dev libffi-dev && \
    apk add --no-cache mariadb-dev

# Application base image.
FROM os-base AS app-base
ADD requirements.txt /opt
RUN pip install -r /opt/requirements.txt && \
    rm /opt/requirements.txt && \
    apk del .build-deps

# Application image.
FROM app-base
ARG SERVER_PORT=8080
ARG REGION_NAME=eu-west-1
ARG SECRET_NAME=rtb-db-secret
ENV SERVER_PORT ${SERVER_PORT}
ENV REGION_NAME ${REGION_NAME}
ENV SECRET_NAME ${SECRET_NAME}
ADD src /opt/src
EXPOSE ${SERVER_PORT}
ENTRYPOINT gunicorn --bind 0.0.0.0:${SERVER_PORT} \
                    --timeout 0 \
                    --workers 3 \
                    --worker-class eventlet \
                    --chdir /opt/src \
                    wsgi:flaskapp
