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

class RequestContext(WebSocketServer):
    def __init__(self):
        super().__init__(8000)

    def request(command, *args):
        request_body = createRequestBody(command, *args)
        self.send(request_body)
        response = self.recv().decode()
        return json.loads(response)


if __name__ == "__main__":
    rc = RequestContext()
    print("Waiting for connection...")
    rc.accept()

    while True:
        response = rc.request("summon", "tnt", "~~~")
        print(response)

