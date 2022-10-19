FROM python:3.10

WORKDIR /opt/app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt requirements.txt

RUN  pip install --upgrade pip \
     && pip install -r requirements.txt

COPY . .

EXPOSE 8000

#for windows
RUN sed -i 's/\r//' docker-entrypoint.sh

RUN chmod +x /opt/app/docker-entrypoint.sh

ENTRYPOINT ["/opt/app/docker-entrypoint.sh"]
