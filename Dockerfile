FROM python:3.10.1-slim

RUN mkdir /usr/cronparser-src
COPY ./cronparser /usr/cronparser-src/cronparser
COPY ./bin /usr/cronparser-src/bin

RUN chmod +x /usr/cronparser-src/bin/cron-parser.py

ENTRYPOINT ["/usr/cronparser-src/bin/cron-parser.py"]
