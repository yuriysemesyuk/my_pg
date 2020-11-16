FROM python:3.7-slim

COPY . /root

WORKDIR /root

ENV TZ=Europe/Kiev

RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD ["gunicorn"  , "-b", "0.0.0.0:5000", "main:app"]

