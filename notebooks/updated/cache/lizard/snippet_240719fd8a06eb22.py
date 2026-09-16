def do_parse(self, arg, fullparse=False):
    from os import path
    fullpath = path.abspath(path.expanduser(arg))
    if path.isdir(fullpath):
        if fullpath[-1] == '/':
            end = -2
        else:
            end = -1
        case = fullpath.split('/')[end]
        self.tests[case] = Analysis(fullpath, fullparse)
        self.do_set(case)
    else:
        msg.err('The folder {} does not exist.'.format(fullpath))