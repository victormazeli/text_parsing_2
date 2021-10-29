import asyncio

from autobahn.asyncio.websocket import WebSocketServerProtocol, \
    WebSocketServerFactory

all_connections = set()


class FacedetectProtocol(WebSocketServerProtocol):

    def onConnect(self, request):
        print("Client connecting: {0}".format(request.peer))
        all_connections.add(self)
        print(type(request), all_connections)

    def onOpen(self):
        print("WebSocket connection open.")

    def onMessage(self, payload, isBinary):
        if isBinary:
            print("Binary message received: {0} bytes".format(len(payload)))
        else:
            print("Text message received: {0}".format(payload.decode('utf8')))

        # echo back message verbatim
        for s in all_connections:
            if s.is_open:
                s.sendMessage(payload, isBinary)
            else:
                all_connections.remove(s)

    def onClose(self, wasClean, code, reason):
        print("WebSocket connection closed: {0}".format(reason))
        all_connections.remove(self)


if __name__ == '__main__':
    factory = WebSocketServerFactory("ws://127.0.0.1:9000")
    factory.protocol = FacedetectProtocol
    print("Initializing web socket server")
    loop = asyncio.get_event_loop()
    coro = loop.create_server(factory, '0.0.0.0', 9000)
    server = loop.run_until_complete(coro)

    try:
        print("Ready to connect")
        loop.run_forever()
    except KeyboardInterrupt:
        print("Closing Web socket server")
        server.close()
        loop.close()
    finally:
        print("Closing Web socket server")
        server.close()
        loop.close()
