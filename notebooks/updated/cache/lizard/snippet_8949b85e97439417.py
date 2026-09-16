def process_file(filename, interval=None, lazy=False):
    mp = MedscanProcessor()
    mp.process_csxml_file(filename, interval, lazy)
    return mp