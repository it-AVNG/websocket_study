'''
Here’s a WebSocket server.
It receives a name from the client, 
sends a greeting, and closes the connection.
'''

import asyncio
import websockets
from icecream import ic

async def hello(websocket):
    # variable : wait for websocket to receive
    name = await websocket.recv()
    # print the variable
    ic("<<< ",name)
    # add greetings str
    greeting = f"greetings, {name}" 
    # send the greeting to the client
    await websocket.send(greeting)
    # print the greetings added
    ic( greeting, " >>>")

async def main():
    async with websockets.serve(hello, "localhost", 8765):
        await asyncio.Future() # run forever
    pass

if __name__ == "__main__":
    asyncio.run(main())