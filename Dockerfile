FROM python:3.10.1-slim

RUN mkdir /usr/cronparser-src
COPY ./cronparser /usr/cronparser-src/cronparser
COPY ./cron-parser.py /usr/cronparser-src/cron-parser.py

RUN chmod +x /usr/cronparser-src/cron-parser.py

ENTRYPOINT ["/usr/cronparser-src/cron-parser.py"]
