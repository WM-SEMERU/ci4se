def create_inline(project, resource, offset):
    pyname = _get_pyname(project, resource, offset)
    message = (
        'Inline refactoring should be performed on a method, local variable or parameter.'
        )
    if pyname is None:
        raise rope.base.exceptions.RefactoringError(message)
    if isinstance(pyname, pynames.ImportedName):
        pyname = pyname._get_imported_pyname()
    if isinstance(pyname, pynames.AssignedName):
        return InlineVariable(project, resource, offset)
    if isinstance(pyname, pynames.ParameterName):
        return InlineParameter(project, resource, offset)
    if isinstance(pyname.get_object(), pyobjects.PyFunction):
        return InlineMethod(project, resource, offset)
    else:
        raise rope.base.exceptions.RefactoringError(message)