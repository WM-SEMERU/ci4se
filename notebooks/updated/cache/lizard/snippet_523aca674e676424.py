def annotatedcore(self):
    logging.info('Calculating annotated core')
    self.total_core()
    for sample in self.metadata:
        if sample.general.bestassemblyfile != 'NA':
            sample[self.analysistype].coreset = set()
            if sample.general.referencegenus == 'Escherichia':
                self.runmetadata.samples.append(sample)
                try:
                    report = sample[self.analysistype].report
                    self.blastparser(report=report, sample=sample,
                        fieldnames=self.fieldnames)
                except KeyError:
                    sample[self.analysistype].coreset = list()
    self.reporter()