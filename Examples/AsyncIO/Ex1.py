import asyncio

async def test():
    print("Hello")
    await asyncio.sleep(1)
    print("world")

async def test_a():
    print("DaVAY")

async def main():
    await asyncio.gather(test(),test_a())
asyncio.run(main())