import asyncio
import websockets
import pathlib
import ssl
from icecream import ic

# setup SSL protocal
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_verify_locations(localhost_pem)


async def hello():
    uri = "wss://localhost:8765"
    # use async connection manager to close the socket
    async with websockets.connect(uri, ssl=ssl_context) as websocket:
        name = input("what is the name: ")
        # send the name through websocket
        await websocket.send(name)
        ic(name, " >>>")
        # wait for receiving a string from server
        res = await websocket.recv()
        # print the display
        ic("<<< ", res)

if __name__ == "__main__":
    asyncio.run(hello())