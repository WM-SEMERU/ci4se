def run(self, steps=None):
    try:
        while self.instruction_pointer < len(self.code):
            self.step()
            if steps is not None:
                steps -= 1
                if steps == 0:
                    break
    except StopIteration:
        pass
    except EOFError:
        pass
    return self