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
c = 0

while True:
    mob = "creeper" if not c % 2 else "lightning_bolt"
    request_body = createRequestBody("summon", mob, "~+5", "~", "~")
    ws.send(request_body)
    response = ws.recv().decode()
    response = json.loads(response)
    print(response["body"]["statusMessage"])
    c += 1

