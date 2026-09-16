def indices(self):
    self._prep_pandas_groupby()

    def extract_group_indices(frame):
        return frame[0], frame[1].index
    return self._mergedRDD.map(extract_group_indices).collectAsMap()