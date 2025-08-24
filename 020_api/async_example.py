import asyncio
import logging
import aiohttp

FORMAT = '[%(asctime)-15s][%(levelname)-8s]%(message)s'
logging.basicConfig(format=FORMAT,level=logging.INFO)
# logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("Starting Example")



async def get_model(model_name,time_to_sleep):
    # Busy waits for a second, but we don't want to stick around...
    logger.info('[get_model][{}] Calling microservice'.format(model_name))
    await asyncio.sleep(time_to_sleep)
    logger.info('[get_model][{}] Returns result'.format(model_name))


"""
async def do_request(url):
    logger.info('[do_request][{}] Calling web'.format(url))
    response = await aiohttp.request(
        'GET', url
    )
    logger.info('[do_request][{}] Returns result:{}'.format(url,response.status))
    return response 
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    #Sleeping example
    loop.run_until_complete(
        asyncio.gather(
            get_model("Modelo A", 2),
            get_model("Modelo B", 1)))

    #http request
    logger.info('\n*************************************************************\nHTTP REQUESTS\n')
    loop.run_until_complete(
        asyncio.gather(
            do_request("http://www.fakeresponse.com/api/?sleep=1"),
            do_request("http://google.es")
        ))

    loop.close()    
    
    """

async def do_request(url):
    logger.info('[do_request][{}] Calling web'.format(url))
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            logger.info('[do_request][{}] Returns result: {}'.format(url, response.status))
            return response


async def main():
    # Sleeping example
    await asyncio.gather(
        get_model("Modelo A", 2),
        get_model("Modelo B", 1)
    )

# HTTP request
    logger.info('\n*************************************************************\nHTTP REQUESTS\n')
    await asyncio.gather(
        do_request("http://www.fakeresponse.com/api/?sleep=1"),
        do_request("http://google.es")
    )


if __name__ == '__main__':
    asyncio.run(main())

