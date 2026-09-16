def connection(self):
    conn = self.session(**self.options)
    try:
        for item in self.middlewares:
            item(conn)
        yield conn
    finally:
        conn.teardown()