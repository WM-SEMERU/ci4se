def load_extra(cls, filename):
    try:
        with open(filename, 'rb') as configuration_file:
            cls.load_extra_data(configuration_file.read())
            sys.stderr.write('Config successfully loaded from {0:s}\n'.
                format(filename))
            return True
    except IOError:
        return False