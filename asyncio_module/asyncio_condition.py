import asyncio

async def consumer(condition,n):
    async with condition:
        print('consumer({}) is waiting'.format(n))
        await condition.wait()
        print('consumer({}) triggered'.format(n))
    print('ending consumer({})'.format(n))
    
async def manipulate_condition(condition):
    print('starting manipulate_condition')
    await asyncio.sleep(0.1) #pause to let consumers start 
    for i in range(1,3):
        async with condition:
            print('notifying {} consumer'.format(i))
            condition.notify(n=i)
        asyncio.sleep(0.1)
        
    async with condition:
        print('notifying remaining consumers')
        condition.notify_all()
    
    print('ending manipulate_condition')
    
async def main(loop):
    #create a condition
    condition = asyncio.Condition()
    #set up tasks watching the condition
    consumers = [asyncio.create_task(consumer(condition,i)) for i in range(5)]
    # schedule a task to manipulate the condition variable
    loop.create_task(manipulate_condition(condition))
    #wait for the consumers to be done
    await asyncio.wait(consumers)
    
if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        result = event_loop.run_until_complete(main(event_loop))
    finally:
        event_loop.close()
    