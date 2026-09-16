def eval_pth(filename, sitedir, dest=None, imports=None):
    if dest is None:
        dest = sys.path
    if not os.path.isfile(filename):
        return
    with open(filename, 'r') as fp:
        for index, line in enumerate(fp):
            if line.startswith('import'):
                if imports is None:
                    exec_pth_import(filename, index + 1, line)
                else:
                    imports.append((filename, index + 1, line))
            else:
                index = line.find('#')
                if index > 0:
                    line = line[:index]
                line = line.strip()
                if not os.path.isabs(line):
                    line = os.path.join(os.path.dirname(filename), line)
                line = os.path.normpath(line)
                if line and line not in dest:
                    dest.insert(0, line)
    return dest