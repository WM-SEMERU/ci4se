def findUiActions(widget):
    import_qt(globals())
    output = []
    for action in widget.findChildren(QtGui.QAction):
        name = nativestring(action.objectName()).lower()
        if name.startswith('ui') and name.endswith('act'):
            output.append(action)
    return output