def indent_selection(self, cursor):
    doc = self.editor.document()
    tab_len = self.editor.tab_length
    cursor.beginEditBlock()
    nb_lines = len(cursor.selection().toPlainText().splitlines())
    c = self.editor.textCursor()
    if c.atBlockStart() and c.position() == c.selectionEnd():
        nb_lines += 1
    block = doc.findBlock(cursor.selectionStart())
    i = 0
    while i < nb_lines:
        nb_space_to_add = tab_len
        cursor = QtGui.QTextCursor(block)
        cursor.movePosition(cursor.StartOfLine, cursor.MoveAnchor)
        if self.editor.use_spaces_instead_of_tabs:
            for _ in range(nb_space_to_add):
                cursor.insertText(' ')
        else:
            cursor.insertText('\t')
        block = block.next()
        i += 1
    cursor.endEditBlock()