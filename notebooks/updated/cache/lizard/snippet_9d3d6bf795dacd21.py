def load_bookmark(self, slot_num):
    bookmarks = CONF.get('editor', 'bookmarks')
    if slot_num in bookmarks:
        filename, line_num, column = bookmarks[slot_num]
    else:
        return
    if not osp.isfile(filename):
        self.last_edit_cursor_pos = None
        return
    self.load(filename)
    editor = self.get_current_editor()
    if line_num < editor.document().lineCount():
        linelength = len(editor.document().findBlockByNumber(line_num).text())
        if column <= linelength:
            editor.go_to_line(line_num + 1, column)
        else:
            editor.go_to_line(line_num + 1, linelength)