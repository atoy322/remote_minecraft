import uuid
import json

from thin_ws_server import WebSocketServer



def createRequestBody(command, *args):
    REQUEST_BODY = {
        "body": {
            "origin": {
                "type": "player"
            },
            "commandLine": command + " " + " ".join(args),
            "version": 1
        },
        "header": {
            "requestId": str(uuid.uuid4()),
            "messagePurpose": "commandRequest",
            "version": 1,
            "messageType": "commandRequest"
        }
    }
    return json.dumps(REQUEST_BODY)

ws = WebSocketServer(8000)
ws.accept()

while True:
    command, args = input("Command: ").split(" ", 1)
    request_body = createRequestBody(command, *args.split(" "))
    ws.send(request_body)
    response = ws.recv().decode()
    response = json.loads(response)
    print(response["body"]["statusMessage"])
