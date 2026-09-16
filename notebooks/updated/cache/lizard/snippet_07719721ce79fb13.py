def highlight_occurences(editor):
    format = editor.language.theme.get('accelerator.occurence')
    if not format:
        return False
    extra_selections = editor.extraSelections() or []
    if not editor.isReadOnly():
        word = editor.get_word_under_cursor()
        if not word:
            return False
        block = editor.document().findBlock(0)
        cursor = editor.document().find(word, block.position(), 
            QTextDocument.FindCaseSensitively | QTextDocument.FindWholeWords)
        while block.isValid() and cursor.position() != -1:
            selection = QTextEdit.ExtraSelection()
            selection.format.setBackground(format.background())
            selection.cursor = cursor
            extra_selections.append(selection)
            cursor = editor.document().find(word, cursor.position(), 
                QTextDocument.FindCaseSensitively | QTextDocument.
                FindWholeWords)
            block = block.next()
    editor.setExtraSelections(extra_selections)
    return True