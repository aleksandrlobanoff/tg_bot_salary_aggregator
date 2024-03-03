import datetime

from utils.db_connect import connect_to_database


# Функция для выполнения агрегации
def aggregate_salary_statistics(dt_from, dt_upto, group_type):
    dt_from_parsed = datetime.datetime.fromisoformat(dt_from)
    dt_upto_parsed = datetime.datetime.fromisoformat(dt_upto)

    collection = connect_to_database()
    if collection is None:
        return None

    # Определение формата группировки
    group_format = {"hour": "%Y-%m-%dT%H", "day": "%Y-%m-%d", "month": "%Y-%m"}.get(
        group_type, "%Y-%m-%d"
    )

    # Подготовка фильтра для запроса
    filter_query = {
        "dt": {
            "$gte": dt_from_parsed,
            "$lte": dt_upto_parsed
        }
    }

    # Агрегация данных в базе данных
    pipeline = [
        {"$match": filter_query},
        {"$group": {
            "_id": {"$dateToString": {"format": group_format, "date": "$dt"}},
            "total_value": {"$sum": "$value"}
        }}
    ]

    result = collection.aggregate(pipeline)

    # Формирование агрегированных данных
    labels = []
    dataset = []

    for doc in result:
        labels.append(doc["_id"])
        dataset.append(doc["total_value"])

    return {"dataset": dataset, "labels": labels}
