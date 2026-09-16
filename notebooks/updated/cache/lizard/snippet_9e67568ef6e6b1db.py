def getPlainText(parent, title, caption, text=''):
    dlg = QDialog(parent)
    dlg.setWindowTitle(title)
    label = QLabel(dlg)
    label.setText(caption)
    edit = QTextEdit(dlg)
    edit.setText(text)
    edit.selectAll()
    opts = QDialogButtonBox.Ok | QDialogButtonBox.Cancel
    btns = QDialogButtonBox(opts, Qt.Horizontal, dlg)
    btns.accepted.connect(dlg.accept)
    btns.rejected.connect(dlg.reject)
    layout = QVBoxLayout()
    layout.addWidget(label)
    layout.addWidget(edit)
    layout.addWidget(btns)
    dlg.setLayout(layout)
    dlg.adjustSize()
    if dlg.exec_():
        return edit.toPlainText(), True
    return '', False