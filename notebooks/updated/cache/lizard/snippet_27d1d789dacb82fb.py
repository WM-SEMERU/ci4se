def get_connection(self):
    conn = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    try:
        conn.bind(self._agent._get_filename())
        conn.listen(1)
        r, addr = conn.accept()
        return r, addr
    except:
        raise