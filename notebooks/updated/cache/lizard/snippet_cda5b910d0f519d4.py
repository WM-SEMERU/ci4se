def is_cell_separator(self, cursor=None, block=None):
    assert cursor is not None or block is not None
    if cursor is not None:
        cursor0 = QTextCursor(cursor)
        cursor0.select(QTextCursor.BlockUnderCursor)
        text = to_text_string(cursor0.selectedText())
    else:
        text = to_text_string(block.text())
    if self.cell_separators is None:
        return False
    else:
        return text.lstrip().startswith(self.cell_separators)