FROM python:3.6

RUN mkdir -p /opt/services/djangoapp
WORKDIR /opt/services/djangoapp

COPY Pipfile Pipfile.lock /opt/services/djangoapp/
RUN pip3 install pipenv && pipenv install --system

COPY . /opt/services/djangoapp

EXPOSE 8000
CMD ["gunicorn", "--bind", ":8000", "config.wsgi"]
