def read(filename):
    return codecs.open(os.path.join(__DIR__, filename), 'r').read()