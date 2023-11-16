import asyncio
import websockets


async def hello():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        message = input("Type a message to send to the server: ")
        await websocket.send(message)
        response = await websocket.recv()
        print(f"Received from server: {response}")

if __name__ == "__main__":
    asyncio.run(hello())
