FROM python:3.9.0

WORKDIR /home/

RUN echo "ha..........jaebal"

RUN git clone https://github.com/KIWONY/Culture-project.git

WORKDIR /home/Culture-project/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c", "python manage.py collectstatic --noinput --settings=dobi.settings.deploy && python manage.py migrate --settings=dobi.settings.deploy && gunicorn dobi.wsgi --env DJANGO_SETTINGS_MODULE=dobi.settings.deploy --bind 0.0.0.0:8000"]