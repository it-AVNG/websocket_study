import asyncio
import websockets
from icecream import ic

async def hello():
    uri = "ws://localhost:8765"
    # use async connection manager to close the socket
    async with websockets.connect(uri) as websocket:
        name = input("what is the name: ")
        # send the name through websocket
        await websocket.send(name)
        ic(name, " >>>")
        # wait for receiving a string from server
        res = await websocket.recv()
        # print the display
        ic("<<< ", res)

async def main():
    while True:
        await hello()
if __name__ == "__main__":
    asyncio.run(main())