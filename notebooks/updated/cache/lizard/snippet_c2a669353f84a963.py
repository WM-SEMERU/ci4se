def is_empty(self):
    return (not self.breakpoint and not self.code_analysis and not self.
        todo and not self.bookmarks)