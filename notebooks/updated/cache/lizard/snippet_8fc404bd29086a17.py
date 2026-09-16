def finalize(self):
    super(StatisticsConsumer, self).finalize()
    self.result = zip(self.grid, map(self.statistics, self.result))