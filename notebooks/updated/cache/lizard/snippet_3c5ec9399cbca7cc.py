def push(self, undoObj):
    if not isinstance(undoObj, QtmacsUndoCommand):
        raise QtmacsArgumentError('undoObj', 'QtmacsUndoCommand', inspect.
            stack()[0][3])
    self._wasUndo = False
    self._push(undoObj)