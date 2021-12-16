# syntax = docker/dockerfile:experimental
FROM python:3.8.2-slim AS base
RUN groupadd -g 3000 -r app \
    && useradd -u 3000 -r -g app -s /usr/sbin/nologin app \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
    ca-certificates=20200601~deb10u2 \
    curl=7.64.0-4+deb10u2 \
    && rm -rf /var/lib/apt/lists/*
WORKDIR /home/src
RUN chown -R app:app /home/src
ENV PYTHONUNBUFFERED=1 \
    PYTHONIOENCODING=UTF-8 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=off \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_VERSION=1.1.3 \
    PATH="/home/src/.poetry/bin:/home/src/.venv/bin:${PATH}" \
    VIRTUAL_ENV="/home/src/.venv"
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/home/src/.poetry python3 -
ENV PATH="${PATH}:/src/.poetry/bin"
COPY --chown=app:app pyproject.toml poetry.lock ./
RUN poetry install -v\
    && poetry run pip install --upgrade pip==21.1.1
COPY --chown=app:app pyproject.toml ./
COPY --chown=app:app tests/ tests/
COPY --chown=app:app src/ src/
EXPOSE 8000