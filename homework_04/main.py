"""
Домашнее задание №4
Асинхронная работа с сетью и бд

доработайте функцию main, по вызову которой будет выполняться полный цикл программы
(добавьте туда выполнение асинхронной функции async_main):
- создание таблиц (инициализация)
- загрузка пользователей и постов
    - загрузка пользователей и постов должна выполняться конкурентно (параллельно)
      при помощи asyncio.gather (https://docs.python.org/3/library/asyncio-task.html#running-tasks-concurrently)
- добавление пользователей и постов в базу данных
  (используйте полученные из запроса данные, передайте их в функцию для добавления в БД)
- закрытие соединения с БД
"""
import asyncio
from jsonplaceholder_requests import fetch_users_data, fetch_posts_data
from models import Base, Post, User, engine, Session


async def create_users(session: Session, users_data: dict) -> list[User]:
    users = [User(
        id=user.get('id'),
        name=user.get('name'),
        username=user.get('username'),
        email=user.get('email')) for user in users_data]

    session.add_all(users)
    await session.commit()
    return users


async def create_posts(session: Session, posts_data: dict) -> list[Post]:
    posts = [Post(
        id=post.get('id'),
        user_id=post.get('userId'),
        title=post.get('title'),
        body=post.get('body')) for post in posts_data]

    session.add_all(posts)
    await session.commit()
    return posts


async def async_main():
    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.drop_all)
        await connection.run_sync(Base.metadata.create_all)

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )

    async with Session() as session:
        await create_users(session, users_data)
        await create_posts(session, posts_data)

    await engine.dispose()


def main():
    asyncio.run(async_main())


if __name__ == "__main__":
    main()
