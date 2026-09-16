def read_file(self, cfgparser, file):
    if hasattr(file, 'readline'):
        if sys.version_info >= (3, 2):
            cfgparser.read_file(file)
        else:
            cfgparser.readfp(file)
    else:
        cfgparser.read(file)