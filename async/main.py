import asyncio
import time


async def waiter():
    task1 = asyncio.create_task(cook('Паста', 8))
    task2 = asyncio.create_task(cook('Салат', 4))
    task3 = asyncio.create_task(cook('Отбивные', 16))

    await task1
    await task2
    await task3


async def cook(order, time_to_prepare):
    print(f'Новый заказ: {order}')
    await asyncio.sleep(time_to_prepare)
    print(order, '- готово через', time_to_prepare)


print(time.strftime('%X'))
asyncio.run(waiter())
print(time.strftime('%X'))
