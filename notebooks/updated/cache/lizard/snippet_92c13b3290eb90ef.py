def feed(self, key_press):
    assert isinstance(key_press, KeyPress)
    self.input_queue.append(key_press)