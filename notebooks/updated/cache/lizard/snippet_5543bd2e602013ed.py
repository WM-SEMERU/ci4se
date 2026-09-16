def localpath(*args):
    plist = [ROOT] + list(args)
    return os.path.abspath(pjoin(*plist))