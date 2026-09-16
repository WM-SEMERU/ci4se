def _increment_current_byte(self):
    if self.tape[self.pointer] is None:
        self.tape[self.pointer] = 1
    elif self.tape[self.pointer] == self.MAX_CELL_SIZE:
        self.tape[self.pointer] = self.MIN_CELL_SIZE
    else:
        self.tape[self.pointer] += 1