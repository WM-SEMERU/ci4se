def get_flagged_args():
    expected = ['os_type', 'os_version']
    arguments = {}
    try:
        opts, adds = getopt.getopt(sys.argv, '', map(lambda x: x + '=',
            expected))
    except getopt.GetoptError as Error:
        print(str(Error))
        print('Defaulting to standard run...')
        return arguments
    for o, a in opts:
        opt = re.sub('^-+', '', o)
        if opt in expected:
            arguments[opt] = a
    if arguments:
        if 'os_type' not in arguments:
            print('Unsupported means of operation!')
            print('You can either specify both os_type and os_version ' +
                'or just os_type')
            arguments = {}
    return arguments