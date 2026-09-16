def Next(self):
    try:
        self.key, self.value = next(self.current)
    except StopIteration:
        if self.current != self.second:
            self.current = self.second
            return self.Next()
        return False
    return True