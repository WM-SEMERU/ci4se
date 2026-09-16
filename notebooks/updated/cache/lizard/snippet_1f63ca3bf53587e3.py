def execute(self, eopatch, data):
    if self.feature_name is None:
        eopatch[self.feature_type] = data
    else:
        eopatch[self.feature_type][self.feature_name] = data
    return eopatch