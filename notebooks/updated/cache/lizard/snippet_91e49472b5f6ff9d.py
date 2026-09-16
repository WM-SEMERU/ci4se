def connect(self):
    if self.sock is not None:
        return
    backoff = 0.01
    while True:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(5)
            sock.connect((self.host, self.port))
            self.sock = sock
            return
        except socket.error:
            time.sleep(random.uniform(0, 2.0 * backoff))
            backoff = min(backoff * 2.0, 5.0)