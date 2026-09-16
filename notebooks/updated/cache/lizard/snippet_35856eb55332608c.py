def _highlight_caret_scope(self):
    cursor = self.editor.textCursor()
    block_nbr = cursor.blockNumber()
    if self._block_nbr != block_nbr:
        block = FoldScope.find_parent_scope(self.editor.textCursor().block())
        try:
            s = FoldScope(block)
        except ValueError:
            self._clear_scope_decos()
        else:
            self._mouse_over_line = block.blockNumber()
            if TextBlockHelper.is_fold_trigger(block):
                self._highlight_block(block)
    self._block_nbr = block_nbr