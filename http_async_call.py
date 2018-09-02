import asyncio
import requests

async def asyncrequestcalls():
    eventloop = asyncio.get_event_loop()

    #make 3 concurrent calls with requests
    responsefuture1 = eventloop.run_in_executor(None, requests.get,'https://webhook.site/c56e4581-762a-45ca-8185-5e1c4b697462')
    responsefuture2 = eventloop.run_in_executor(None, requests.get,'https://webhook.site/c56e4581-762a-45ca-8185-5e1c4b697462')
    responsefuture3 = eventloop.run_in_executor(None, requests.get,'https://webhook.site/c56e4581-762a-45ca-8185-5e1c4b697462')

    #wait for responses
    response1  = await responsefuture1
    print(response1.headers.get('Date'))
          
    response2  = await responsefuture2
    print(response2.headers.get('Date'))
         
    response3  = await responsefuture3
    print(response3.headers.get('Date'))         
   
eventloop = asyncio.get_event_loop()
eventloop.run_until_complete(asyncrequestcalls())
    