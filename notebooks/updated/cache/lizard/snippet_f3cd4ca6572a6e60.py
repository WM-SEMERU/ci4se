def insert(self, s):
    for c in s:
        self.text.insert(self.cursor_loc, c)
        self.cursor_loc += 1