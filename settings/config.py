import os

# -----------------------------------------------------------
#  Env variables and checking for their presence
# -----------------------------------------------------------

# Telegram
BOT_TOKEN = os.getenv('BOT_TOKEN')
if not BOT_TOKEN:
    raise ValueError('Missing required environment variable: BOT_TOKEN')

# Postgres
POSTGRES_USER = os.getenv('POSTGRES_USER')
if not POSTGRES_USER:
    raise RuntimeError('Missing required environment variable: POSTGRES_USER')

POSTGRES_PASSWORD = os.getenv('POSTGRES_PASSWORD')
if not POSTGRES_PASSWORD:
    raise RuntimeError('Missing required environment variable: POSTGRES_PASSWORD')

POSTGRES_DB = os.getenv('POSTGRES_DB', "app")
