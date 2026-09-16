def hasNext(self):
    cursor_pos = self.cursorpos + 1
    try:
        self.cursordat[cursor_pos]
        return True
    except IndexError:
        return False