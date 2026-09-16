def get_stats(self, stat_name):
    return [self.get_stat(r, stat_name) for r in self.statistics.keys()]