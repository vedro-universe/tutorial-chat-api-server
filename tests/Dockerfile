FROM python:3.10-alpine

WORKDIR /e2e

RUN pip3 install pip --upgrade

COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .
