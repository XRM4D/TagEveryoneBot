FROM python:3.13-slim

RUN apt-get update && apt-get install -y \
      libpq-dev python3-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir poetry
ENV PATH="/root/.local/bin:$PATH"
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root --no-interaction --no-ansi

COPY . .
CMD ["python3", "main.py"]