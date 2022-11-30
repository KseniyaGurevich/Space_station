FROM python:3.7-slim

ENV POETRY_VIRTUALENVS_CREATE=false
RUN mkdir /app
WORKDIR /app
COPY poetry.lock poetry.lock
COPY pyproject.toml pyproject.toml
RUN pip3 install poetry
RUN poetry install --no-root
COPY station/ /app

# CMD ["pip3", "freeze"]
CMD ["python3", "manage.py", "runserver", "0:8000"]
#CMD ["gunicorn", "recipes.wsgi:application", "--bind", "0:8000" ]