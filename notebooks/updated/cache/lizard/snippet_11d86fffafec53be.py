def changed(self, src, path, dest):
    try:
        mtime = os.path.getmtime(os.path.join(src, path))
        self._build(src, path, dest, mtime)
    except EnvironmentError as e:
        logging.error('{0} is inaccessible: {1}'.format(termcolor.colored(
            path, 'yellow', attrs=['bold']), e.args[0]))