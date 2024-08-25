FROM python:3.12-alpine
RUN apk update && apk upgrade

WORKDIR /app
# ENTRYPOINT ["python", "service/main.py"]
ENTRYPOINT ["sh", "./entrypoint.sh"]