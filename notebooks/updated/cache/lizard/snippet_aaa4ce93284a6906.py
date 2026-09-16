def name(self):
    try:
        return TIFF.TAGS[self.code]
    except KeyError:
        return str(self.code)