import json
from aiogram import types


async def start(message: types.Message):

    await message.reply(
        f"Hi {message.from_user.first_name}! Отправь мне параметры для агрегации статистики о зарплатах."
    )


async def process_message(message: types.Message):

    from utils.aggregation import aggregate_salary_statistics

    try:
        params = json.loads(message.text)
        dt_from = params['dt_from']
        dt_upto = params['dt_upto']
        group_type = params['group_type']

        result = aggregate_salary_statistics(dt_from, dt_upto, group_type)

        if result:
            output = json.dumps(result)
            await message.reply(output)
        else:
            example_request = (
                '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}'
            )
            await message.reply(f"Невалидный запрос. Пример запроса:\n{example_request}")
    except json.JSONDecodeError:
        example_request = (
            '{"dt_from": "2022-09-01T00:00:00", "dt_upto": "2022-12-31T23:59:00", "group_type": "month"}'
        )
        await message.reply(f"Невалидный запрос. Пример запроса:\n{example_request}")
    except Exception as e:
        await message.reply(f"Произошла ошибка: {e}")
