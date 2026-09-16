def fullscreen(self):
    self.stream.write(self.enter_fullscreen)
    try:
        yield
    finally:
        self.stream.write(self.exit_fullscreen)