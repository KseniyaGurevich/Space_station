FROM python:3.7-slim

ENV POETRY_VIRTUALENVS_CREATE=false
RUN mkdir /app
WORKDIR /app
COPY ../poetry.lock poetry.lock
COPY ../pyproject.toml pyproject.toml
RUN pip3 install poetry
RUN poetry install --no-root
COPY ../station/ /app

CMD ["gunicorn", "station.wsgi:application", "--bind", "0:8000" ]