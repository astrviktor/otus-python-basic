"""
создайте асинхронные функции для выполнения запросов к ресурсам (используйте aiohttp)
"""
from aiohttp import ClientSession

USERS_DATA_URL = "https://jsonplaceholder.typicode.com/users"
POSTS_DATA_URL = "https://jsonplaceholder.typicode.com/posts"


async def fetch_api(url: str) -> dict:
    async with ClientSession() as session:
        async with session.get(url) as response:
            data: dict = await response.json()
            return data


async def fetch_users_data() -> dict:
    data: dict = await fetch_api(USERS_DATA_URL)
    return data


async def fetch_posts_data() -> dict:
    data: dict = await fetch_api(POSTS_DATA_URL)
    return data

