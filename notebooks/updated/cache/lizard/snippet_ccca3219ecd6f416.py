def getFilenames(self, pixels=None):
    logger.debug('Getting filenames...')
    if pixels is None:
        return self.filenames
    else:
        return self.filenames[np.in1d(self.filenames['pix'], pixels)]