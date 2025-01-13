from peewee import PostgresqlDatabase
import os
from dotenv import load_dotenv

load_dotenv()
db = PostgresqlDatabase(os.getenv('database_uri',''))
