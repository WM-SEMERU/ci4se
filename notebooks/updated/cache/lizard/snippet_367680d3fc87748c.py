def _move_to_top(self, pos):
    if pos > 0:
        self.queue.rotate(-pos)
        item = self.queue.popleft()
        self.queue.rotate(pos)
        self.queue.appendleft(item)