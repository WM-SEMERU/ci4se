def get_colormap(cls, names=[], N=10, *args, **kwargs):
    names = safe_list(names)
    obj = cls(names, N, *args, **kwargs)
    vbox = obj.layout()
    buttons = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.
        Cancel, parent=obj)
    buttons.button(QDialogButtonBox.Ok).setEnabled(False)
    vbox.addWidget(buttons)
    buttons.accepted.connect(obj.accept)
    buttons.rejected.connect(obj.reject)
    obj.table.selectionModel().selectionChanged.connect(lambda indices:
        buttons.button(QDialogButtonBox.Ok).setEnabled(bool(indices)))
    accepted = obj.exec_()
    if accepted:
        return obj.table.chosen_colormap