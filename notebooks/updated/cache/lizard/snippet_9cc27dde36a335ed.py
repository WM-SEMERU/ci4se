def autodoc_module(module):
    doc = getattr(module, '__doc__')
    if doc is None:
        doc = ''
    members = []
    for name, member in inspect.getmembers(module):
        if not name.startswith('_') and inspect.getmodule(member) is module:
            members.append((name, member))
    members = sorted(members, key=_number_of_line)
    if members:
        lines = [
            '\n\nModule :mod:`~%s` implements the following members:\n' %
            module.__name__]
        for name, member in members:
            if inspect.isfunction(member):
                type_ = 'func'
            elif inspect.isclass(member):
                type_ = 'class'
            else:
                type_ = 'obj'
            lines.append('      * :%s:`~%s` %s' % (type_, name, objecttools
                .description(member)))
        doc = doc + '\n\n' + '\n'.join(lines) + '\n\n' + 80 * '_'
        module.__doc__ = doc