def receive_data_chunk(self, raw_data, start):
    self.file.write(raw_data)
    eventlet.sleep(0)