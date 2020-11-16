FROM python:3.8-slim-buster
WORKDIR /app
COPY Pipfile* /app/
RUN pip install pipenv
RUN pipenv install
COPY . /app/
ENTRYPOINT ["./docker-entrypoint.sh"]
