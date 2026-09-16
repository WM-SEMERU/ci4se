def _computeUniqueReadCounts(self):
    for pathogenName, samples in self.pathogenNames.items():
        for sampleName in samples:
            self.pathogenSampleFiles.add(pathogenName, sampleName)