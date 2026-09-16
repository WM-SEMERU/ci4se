def write(self, data):
    try:
        self.connection.sendall(data)
    except socket.error:
        self.close()
        raise