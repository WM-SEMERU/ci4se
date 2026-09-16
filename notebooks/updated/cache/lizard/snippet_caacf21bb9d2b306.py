def hidden_cursor(self):
    self.stream.write(self.hide_cursor)
    try:
        yield
    finally:
        self.stream.write(self.normal_cursor)