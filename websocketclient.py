from websocket import create_connection

WEBSOCKET_URL = "ws://localhost:9000/"

ws = create_connection(WEBSOCKET_URL)
print("Sending Alarm")
#ws.send("FACE_DETECTED")
ws.send("NONE")
print("Sent")
result =  ws.recv()
print("Received '%s'" % result)
ws.close()
