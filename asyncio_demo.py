import asyncio

async def say_hello():
    print("Hello")
    await asyncio.sleep(1)  # 非同步等待 1 秒
    print("World")

async def main():
    await say_hello()

# 執行非同步任務
asyncio.run(main())


# pip install aiohttp

