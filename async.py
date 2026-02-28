import asyncio

async def task(name, delay):
    await asyncio.sleep(delay)
    print(f"Task {name} completed")

async def main():
    await asyncio.gather(
        task("A", 2),
        task("B", 1)
    )

asyncio.run(main())