def Terminate(self):
    self.lock.acquire()
    try:
        for bucket in self.connections.values():
            try:
                for conn in bucket:
                    conn.lock()
                    try:
                        conn.Close()
                    except Exception:
                        pass
                    conn.release()
            except Exception:
                pass
        self.connections = {}
    finally:
        self.lock.release()