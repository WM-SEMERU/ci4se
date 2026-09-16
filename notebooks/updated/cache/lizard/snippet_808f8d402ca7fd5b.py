def execute(self, eopatch):
    feature_type, feature_name = next(self.feature(eopatch))
    eopatch[feature_type][feature_name] = self.process(eopatch[feature_type
        ][feature_name])
    return eopatch