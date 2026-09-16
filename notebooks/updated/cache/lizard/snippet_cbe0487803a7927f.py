def binPack(self, jobShapes):
    logger.debug('Running bin packing for node shapes %s and %s job(s).',
        self.nodeShapes, len(jobShapes))
    jobShapes.sort()
    jobShapes.reverse()
    assert len(jobShapes) == 0 or jobShapes[0] >= jobShapes[-1]
    for jS in jobShapes:
        self.addJobShape(jS)