def create_comment_edit(self):
    pte = JB_PlainTextEdit(parent=self)
    pte.set_placeholder('Enter a comment before saving...')
    pte.setMaximumHeight(120)
    return pte