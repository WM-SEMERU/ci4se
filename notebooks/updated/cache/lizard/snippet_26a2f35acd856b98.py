def rotate(self, steps):
    popped_deque = self.pop(steps)
    if steps >= 0:
        return popped_deque.extendleft(islice(self.reverse(), steps))
    return popped_deque.extend(islice(self, -steps))