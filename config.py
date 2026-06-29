import os
from dotenv import load_dotenv

load_dotenv()


print("DB_HOST =", os.getenv("MYSQL_HOST"))
print("DB_USER =", os.getenv("MYSQL_USER"))
print("DB_PASSWORD =", os.getenv("MYSQL_PASSWORD"))
print("DB_NAME =", os.getenv("MYSQL_DATABASE"))

class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    DB_HOST = os.getenv("MYSQL_HOST")
    DB_USER = os.getenv("MYSQL_USER")
    DB_PASSWORD = os.getenv("MYSQL_PASSWORD")
    DB_NAME = os.getenv("MYSQL_DATABASE")