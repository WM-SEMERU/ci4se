def handle_transform(self, task):
    self.transformed += 1
    file = task.result()
    if file:
        self.next.append_file(file)
    self.flush_if_ended()