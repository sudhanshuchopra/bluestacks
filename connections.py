import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.pool import NullPool

# Loading .env variables into environment
load_dotenv()

DB_URL = os.getenv('DB_URL')
engine = create_engine(DB_URL, poolclass=NullPool)
