FROM python:3.13-slim

LABEL authors="denisgloba"

# Install Poetry and other build dependencies
RUN apt-get update && apt-get install -y curl build-essential \
    && curl -sSL https://install.python-poetry.org | python3 - \
    && apt-get purge -y curl \
    && apt-get autoremove -y \
    && rm -rf /var/lib/apt/lists/*

# Add poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Prevent poetry from creating virtualenvs
ENV POETRY_VIRTUALENVS_CREATE=false

WORKDIR /app

# Copy only dependency files first to leverage Docker cache
COPY pyproject.toml poetry.lock* ./

# Install Python dependencies
RUN poetry install --no-root --no-interaction --no-ansi

# Copy the rest of the app
COPY . .

CMD ["python3", "main.py"]