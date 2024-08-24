FROM python:3.12-alpine
RUN apk update && apk upgrade
WORKDIR /service
ENTRYPOINT ["python", "service/main.py"]