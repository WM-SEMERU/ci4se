def _run_with_different_python(executable):
    args = [arg for arg in sys.argv if arg != VIRTUALENV_OPTION]
    args.insert(0, executable)
    print('Running bootstrap.py with {0}'.format(executable))
    exit(subprocess.call(args))