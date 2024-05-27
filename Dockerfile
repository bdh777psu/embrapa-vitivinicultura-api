FROM python:3.10-slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

ENV HOST 0.0.0.0

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

ENTRYPOINT ["python"]

CMD ["-m", "swagger_server"]
