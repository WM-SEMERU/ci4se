def show_env(environment):
    if not environment:
        print('You need to supply an environment name')
        return
    parser = read_config()
    try:
        commands = parser.get(environment, 'cmd').split('\n')
    except KeyError:
        print("Unknown environment type '%s'" % environment)
        return
    print('Environment: %s\n' % environment)
    for cmd in commands:
        print(cmd)