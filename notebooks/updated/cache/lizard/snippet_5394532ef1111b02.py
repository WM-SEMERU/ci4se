def activated(self, item):
    editor_item = self.editor_items.get(self.editor_ids.get(self.
        current_editor))
    line = 0
    if item == editor_item:
        line = 1
    elif isinstance(item, TreeItem):
        line = item.line
    self.freeze = True
    root_item = self.get_root_item(item)
    if line:
        self.parent().edit_goto.emit(root_item.path, line, item.text(0))
    else:
        self.parent().edit.emit(root_item.path)
    self.freeze = False
    parent = self.current_editor.parent()
    for editor_id, i_item in list(self.editor_items.items()):
        if i_item is root_item:
            for editor, _id in list(self.editor_ids.items()):
                if _id == editor_id and editor.parent() is parent:
                    self.current_editor = editor
                    break
            break