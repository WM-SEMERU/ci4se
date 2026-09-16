def publish(self, name, data, userList):
    self.broadcast(userList, {'name': name, 'data': SockJSDefaultHandler.
        _parser.encode(data)})