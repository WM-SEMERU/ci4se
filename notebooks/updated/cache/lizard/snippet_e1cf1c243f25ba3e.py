def transform_annotation(self, ann, duration):
    intervals, values = ann.to_interval_values()
    tags = []
    for v in values:
        if v in self._classes:
            tags.extend(self.encoder.transform([[v]]))
        else:
            tags.extend(self.encoder.transform([[]]))
    tags = np.asarray(tags)
    target = self.encode_intervals(duration, intervals, tags)
    return {'tags': target}