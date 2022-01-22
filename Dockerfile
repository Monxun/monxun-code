FROM python:3.6

RUN apt-get update -y && \
    apt-get install -y git

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./app /code/app

CMD python app/manage.py runserver 8300