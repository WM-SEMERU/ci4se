def dataframe(self, only_successful=True):

    def extract(r):
        if r[Experiment.METADATA][Experiment.STATUS]:
            rd = r[Experiment.METADATA].copy()
            rd.update(r[Experiment.PARAMETERS])
            rd.update(r[Experiment.RESULTS])
        elif not only_successful:
            rd = r[Experiment.METADATA].copy()
            rd.update(r[Experiment.PARAMETERS])
        else:
            rd = None
        return rd
    records = [r for r in map(extract, self.results()) if r is not None]
    return DataFrame.from_records(records)