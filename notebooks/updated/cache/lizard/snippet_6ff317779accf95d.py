def get_surrounding_blocks(self):
    next = self.next_blocks()
    prev = self.previous_blocks()
    surrounding_blocks = list(chain(prev, [self], next))
    return surrounding_blocks