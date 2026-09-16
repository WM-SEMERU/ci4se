def addStreamHandler(self, lvl=20):
    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(lvl)
    sFrmt = logging.Formatter('%(message)s')
    if False:
        sFrmt = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    sh.setFormatter(sFrmt)
    self.addHandler(sh)