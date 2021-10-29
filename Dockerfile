FROM python:3.7-alpine3.9

WORKDIR /app

RUN apk add --update build-base git make

RUN apk update \
    && apk add --virtual build-deps gcc musl-dev \
    && apk add jpeg-dev zlib-dev libjpeg \
    && apk add tesseract-ocr \
    && apk del build-deps


RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

RUN apk update

WORKDIR /app
COPY . /app

ENTRYPOINT ["python3.7", "run.py"]
