def peek(self, length):
    t = self.current_position + length
    if not self.current_segment.inrange(t):
        raise Exception('Would read over segment boundaries!')
    return self.current_segment.data[self.current_position - self.
        current_segment.start_address:t - self.current_segment.start_address]