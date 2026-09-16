def src_builder(self):
    try:
        scb = self.sbuilder
    except AttributeError:
        scb = self.dir.src_builder()
        self.sbuilder = scb
    return scb