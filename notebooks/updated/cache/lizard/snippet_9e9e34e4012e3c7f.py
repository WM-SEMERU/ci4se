def parse_requirements(requirements_file):
    if os.path.exists(requirements_file):
        return open(requirements_file, 'r').read().splitlines()
    else:
        print('ERROR: requirements file ' + requirements_file + ' not found.')
        sys.exit(1)