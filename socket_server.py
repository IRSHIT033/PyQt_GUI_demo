import websockets
import asyncio
import random
# Server data
PORT = 7890
print("Server listening on Port " + str(PORT))

machine_hazards: list[str] = ["Air Probe Faliure", "Skin Probe Faliure",
                              "Temperature High", "Temperature Low", "Heater Faliure"]


async def echo(websocket, path):
    print("A client just connected")
    try:
        time: int = 2
        while True:
            await asyncio.sleep(time)
            await websocket.send(random.choice(machine_hazards))
            msg = await websocket.recv()
            if msg == "Mute_alarms":
                time = 10
                print("muting alarms")
    # Handle disconnecting clients
    except websockets.exceptions.ConnectionClosed as e:
        print("A client just disconnected")

# Start the server
start_server = websockets.serve(echo, "localhost", PORT)
asyncio.run(start_server)
