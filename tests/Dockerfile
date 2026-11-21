FROM python:3.14.10-alpine3.24

WORKDIR /e2e

RUN pip3 install pip --upgrade

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
