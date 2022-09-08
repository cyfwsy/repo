import asyncio
import functools

def unlock(lock):
    print('callback releasing lock')
    lock.release()
    
async def coro1(lock):
    print('coro1 waiting for the lock')
    async with lock:
        print('coro1 acquired the lock')
    print('coro1 release the lock')
    
async def coro2(lock):
    print('coro2 waiting for the lock')
    await lock.acquire()
    try:
        print('coro2 acquired lock')
    finally:
        print('coro2 release lock')
        lock.release()
        
async def main(loop):
    #create and acquire a shared lock
    lock = asyncio.Lock()
    print('acquiring the lock before staring coroutines')
    await lock.acquire()
    print('lock acquired {}'.format(lock.locked()))
    
    #schedule a callback to unlock the lock
    loop.call_later(0.1,functools.partial(unlock,lock))
    
    #run the coroutines that want to use the lock
    print('waiting for coroutines')
    await asyncio.wait([asyncio.create_task(coro1(lock)),
                        asyncio.create_task(coro2(lock))])
    
if __name__ == '__main__':
    event_loop = asyncio.get_event_loop()
    try:
        event_loop.run_until_complete(main(event_loop))
    finally:
        event_loop.close()
    
        