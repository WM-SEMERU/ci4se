def _process_arguments(self, arguments):
    if not arguments:
        return None
    a = arguments.split(' :', 1)
    arglist = a[0].split()
    if len(a) == 2:
        arglist.append(a[1])
    return arglist