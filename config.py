# Configring the connection to the SQL Server database
import os
from dotenv import load_dotenv

load_dotenv()

HOST = "localhost"
PORT = 3306
USER = "root"
PASSWORD = os.getenv("DB_PASSWORD")
DATABASE = "creater_analytics"