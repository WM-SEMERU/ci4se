def check(self, feature):
    mapper = feature.as_dataframe_mapper()
    mapper.fit(self.X, y=self.y)