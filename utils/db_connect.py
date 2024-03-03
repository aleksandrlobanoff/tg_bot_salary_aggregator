import pymongo
from dotenv import load_dotenv
import os

# Загрузить переменные из файла .env
load_dotenv()

# Получить данные для подключения к базе данных из переменных окружения
mongodb_host = os.getenv("MONGODB_HOST")
db_name = os.getenv("MONGODB_DATABASE")
collection_name = "test"


# Подключение к базе данных
def connect_to_database():
    try:
        client = pymongo.MongoClient(mongodb_host)
        db = client[db_name]
        collection = db[collection_name]
        return collection
    except Exception as e:
        print("Ошибка подключения к базе данных:", str(e))
        return None
