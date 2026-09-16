def main(self):
    try:
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind((self.host, self.port))
        self.sock.listen(5)
        self.sock.settimeout(END_RESP)
        self.stop = self.terminate = False
        while not (self.stop or self.terminate):
            try:
                conn, addr = self.sock.accept()
            except socket.error:
                pass
            except KeyboardInterrupt:
                self.terminate_server()
            else:
                threaded(self._handler, (conn,))
        while not self.terminate:
            time.sleep(END_RESP)
    finally:
        self.sock.close()