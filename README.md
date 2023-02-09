# Basic and Full-text Search with Django and Postgres

## Apache Tika

- Populate data: $ python manage.py add_tika

tika-python: This API is binding to Apache Tika REST services, At the initial, API launches a tika-server instance, the extraction request will consume and process in the server. If you try tika-app.jar instead of **tika-server.jar**, it is not going to be worked. https://github.com/chrismattmann/tika-python

- References
https://github.com/kimtth/pyspark-tika-text-extraction
https://medium.com/mlearning-ai/convert-any-type-of-document-to-text-with-apache-tika-using-python-api-ff306c467b3

- download https://tika.apache.org/download.html

https://www.apache.org/dyn/closer.lua/tika/2.7.0/tika-server-standard-2.7.0.jar

https://pypi.org/project/tika/

set the TIKA_SERVER_JAR environment variable to TIKA_SERVER_JAR="file:////tika-server.jar" which successfully tells python-tika to "download" this file and move it to /tmp/tika-server.jar and run as background process.

- reset database: ./manage.py reset_db --noinput --close-sessions


## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/django-search/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Apply the migrations and seed the database:

```sh
$ docker-compose exec web python manage.py migrate
$ docker-compose exec web python manage.py add_contents
```

Navigate to [http://127.0.0.1:8011/contents/](http://127.0.0.1:8011/contents/).


## Basic vs Full-text Search

You can see examples of both basic and full-text search in *contents/views.py*.
