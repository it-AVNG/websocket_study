import asyncio
import websockets
from icecream import ic
import pathlib
import ssl

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

# load certificates
ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
localhost_pem = pathlib.Path(__file__).with_name("localhost.pem")
ssl_context.load_cert_chain(localhost_pem)

async def main():
    async with websockets.serve(hello,"localhost", 8765, ssl=ssl_context):
        await asyncio.Future() 

if __name__ == "__main__":
    asyncio.run(main())