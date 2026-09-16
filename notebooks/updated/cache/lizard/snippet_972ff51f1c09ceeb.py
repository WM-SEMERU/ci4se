def put(self, message):
    return self.connection.put('echo/string', data=dict(message=message))