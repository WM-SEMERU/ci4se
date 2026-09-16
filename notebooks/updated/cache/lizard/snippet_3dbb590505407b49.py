def goto_line(self, line, column=0, move=True):
    text_cursor = self.move_cursor_to(line)
    if column:
        text_cursor.movePosition(text_cursor.Right, text_cursor.MoveAnchor,
            column)
    if move:
        block = text_cursor.block()
        try:
            folding_panel = self._editor.panels.get('FoldingPanel')
        except KeyError:
            pass
        else:
            from pyqode.core.api.folding import FoldScope
            if not block.isVisible():
                block = FoldScope.find_parent_scope(block)
                if TextBlockHelper.is_collapsed(block):
                    folding_panel.toggle_fold_trigger(block)
        self._editor.setTextCursor(text_cursor)
    return text_cursor