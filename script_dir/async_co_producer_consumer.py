import asyncio
async def consumer(n,q):
    print('consumer {}:starting'.format(n))
    while True:
        print('consumer {}:waiting for item'.format(n))
        item = await q.get()
        print('consumer {}: has item {}'.format(n,item))
        if item is "STOP":
            # 'stop' is the signal to stop.
            q.task_done()
            break
        else:
            await asyncio.sleep(0.01 * item)
            q.task_done()
        print('consumer {}: ending'.format(n))


async def producer(q,num_consumers):
    print('producer: starting')
    #Add some numbers to the queue to simulate jobs.
    for i in range(num_consumers * 3):
        await q.put(i)
        print('producer: add task {} to the queue'.format(i))
    #Add None entries in the queue to signal the consumer to exit
    print('producer: adding stop signal to the queue')
    for i in range(num_consumers):
        await q.put('STOP')
    print('producer: waiting for queue to empty')
    await q.join()
    print('producer ending')

async def main(loop,num_consumers):
    #Create the queue with a fixed size so the producer will block until
    #the consumer pull some items out.
    q = asyncio.Queue(maxsize=2)

    #schedule the producer task
    consumers = [loop.create_task(consumer(i,q)) for i in range(num_consumers)]
    prod = loop.create_task(producer(q,num_consumers))
    #wait for all of the coroutines to finish
    await asyncio.wait(consumers + [prod])

event_loop = asyncio.get_event_loop()
try:
    event_loop.run_until_complete(main(event_loop,3))
finally:
    event_loop.close()



