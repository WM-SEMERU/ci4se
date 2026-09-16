def load(self, filename):
    try:
        with open(filename, 'rb') as fp:
            self.counters = cPickle.load(fp)
    except:
        logging.debug("can't load counter from file: %s", filename)
        return False
    return True