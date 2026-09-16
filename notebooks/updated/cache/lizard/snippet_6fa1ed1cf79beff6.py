def _on_action_toggle(self):
    block = FoldScope.find_parent_scope(self.editor.textCursor().block())
    self.toggle_fold_trigger(block)