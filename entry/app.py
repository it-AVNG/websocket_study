import asyncio
import itertools
import websockets
import json

# async def handler(websocket):
#     while True:
#         message = await websocket.recv()
#         print(message)

# async def handler(websocket):
#     while True:
#         try:
#             message = await websocket.recv()
#         except websockets.ConnectionClosedOK:
#             break
#         print(message)

from connect4 import PLAYER1, PLAYER2, Connect4

async def handler(websocket):
    # init a game
    game = Connect4()

    #players take turns using the browser
    turns = itertools.cycle([PLAYER1, PLAYER2])
    player = next(turns)

    async for message in websocket:
        # PARSE a "play" event from the UI
        event = json.loads(message)
        assert event["type"] == "play"
        column = event["column"]

        try:
            #play the move
            row = game.play(player, column)
        except RuntimeError as e:
            # send error event if the move illegal
            event = {
                "type": "error",
                "message": str(e),
            }
            await websocket.send(json.dumps(event))
            continue

        # Send a "play" event to update the UI.
        event = {
            "type": "play",
            "player": player,
            "column": column,
            "row": row,
        }

        await websocket.send(json.dumps(event))

        # if move is winning sen "win"
        if game.winner is not None:
            event = {
                "type": "win",
                "player": game.winner,
            }
            await websocket.send(json.dumps(event))

        #alternate turns.
        player =next(turns)

async def main():
    async with websockets.serve(handler, "", 8001):
        await asyncio.Future()  # run forever


if __name__ == "__main__":
    asyncio.run(main())