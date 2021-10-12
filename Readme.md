# Minecraft Remote Controller
This repository is example of [thin_ws_server](https://github.com/atoy322/ws_server).

## Get started
```shell
git clone https://github.com/atoy322/remote_minecraft
pip install thin-ws-server
cd remote_minecraft
```

## Usage
1. launch websocket server
```python
from requester import CommandRequester

cr = CommandRequester()
cr.accept()  # accept client connection
cr.request("setblock", "~~~", "tnt")  # run setblock command
cr.close()  # connection close
```
2. Run below command in minecraft.
```shell
/connect {YOUR IP}:8000
```
3. You can remote control the Minecraft.

not completed.
