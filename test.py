import asyncio

async def swap_polarity():
    while 1:
        print('swap polarity')
        await asyncio.sleep(10)
    return

async def print_numbers():
    for i in range(10):
        print(i)
        await asyncio.sleep(0.25)
        
async def main():
    task1 = asyncio.create_task(swap_polarity())
    task2 = asyncio.create_task(print_numbers())
    
    await task1
    await task2



asyncio.run(main())