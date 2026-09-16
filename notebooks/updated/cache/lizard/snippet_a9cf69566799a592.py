def setupQuery(self, query, op, editor):
    try:
        registry = self._operatorMap[nativestring(op)]
    except KeyError:
        return False
    op = registry.op
    value = registry.defaultValue
    if op is None:
        return False
    if editor is not None:
        value = self.editorValue(editor)
    query.setOperatorType(op)
    query.setValue(value)
    return True