import pymongo
from dotenv import load_dotenv
import os


def connect_to_mongodb():
    try:
        # Загрузка переменных окружения из файла .env
        load_dotenv()

        # Чтение переменных окружения
        host = os.getenv('MONGODB_HOST')
        port_str = os.getenv('MONGODB_PORT')
        username = os.getenv('MONGODB_USERNAME')
        password = os.getenv('MONGODB_PASSWORD')
        database = os.getenv('MONGODB_DATABASE')

        # Проверка значений переменных окружения
        if not (host and username and password and database):
            raise ValueError("Не все данные для подключения к MongoDB указаны.")

        # Установка соединения с базой данных MongoDB
        client = pymongo.MongoClient(host=host, port=int(port_str), username=username, password=password)

        # Проверка фактического подключения
        client.server_info()

        # Выбор базы данных
        db = client[database]

        # Возвращаем подключение и базу данных
        return client, db

    except (pymongo.errors.ConnectionFailure, ValueError) as e:
        print('Не удалось подключиться к серверу MongoDB.')
        print(e)


# Пример использования функции подключения
client, db = connect_to_mongodb()

# Проверка подключения к базе данных
if client is not None and db is not None:
    print('Подключение к MongoDB успешно установлено.')
else:
    print('Не удалось подключиться к MongoDB.')
