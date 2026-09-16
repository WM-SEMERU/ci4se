def start(self):
    if self.state != STATE_RUNNING:
        conn = self.loop.create_connection(lambda : self, self.host, self.port)
        task = self.loop.create_task(conn)
        task.add_done_callback(self.init_done)
        self.state = STATE_STARTING