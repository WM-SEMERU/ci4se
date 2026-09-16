def dir_cmd(argv):
    env = parse_envname(argv, lambda : sys.exit(
        'You must provide a valid virtualenv to target'))
    print(workon_home / env)