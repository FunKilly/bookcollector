# syntax = docker/dockerfile:experimental
FROM python:3.10.6-slim-buster AS base
RUN apt-get update \
    && apt-get install -y --no-install-recommends  \
    ca-certificates \
    curl \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /home/testfastapi
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VERSION=1.1.15 \
    PATH="/home/testfastapi/.poetry/bin:/home/testfastapi/.venv/bin:${PATH}" \
    VIRTUAL_ENV="/home/src/.venv"
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
ENV PATH="${PATH}:/root/.poetry/bin"
COPY pyproject.toml .
COPY poetry.lock .
RUN poetry config virtualenvs.create false  && poetry install --no-interaction --no-ansi\
    && poetry run pip install --upgrade pip==21.1.1
COPY tests/ tests/
COPY src/ src/
WORKDIR /home/testfastapi/src
CMD ["uvicorn", "portal.endpoints.routes:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
