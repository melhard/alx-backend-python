import asyncio
import aiosqlite

DATABASE = "my_database.db"

async def async_fetch_users():
    async with aiosqlite.connect(DATABASE) as db:
        cursor = await db.execute("SELECT * FROM users")
        users = await cursor.fetchall()
        await cursor.close()
        print("All users:", users)
        return users

async def async_fetch_older_users():
    async with aiosqlite.connect(DATABASE) as db:
        cursor = await db.execute("SELECT * FROM users WHERE age > 40")
        older_users = await cursor.fetchall()
        await cursor.close()
        print("Users older than 40:", older_users)
        return older_users

async def fetch_concurrently():
    await asyncio.gather(
        async_fetch_users(),
        async_fetch_older_users()
    )

if __name__ == "__main__":
    asyncio.run(fetch_concurrently())
