def split_input(args):
    args['files'] = []
    args['urls'] = []
    for arg in args['query']:
        if os.path.isfile(arg):
            args['files'].append(arg)
        else:
            args['urls'].append(arg.strip('/'))