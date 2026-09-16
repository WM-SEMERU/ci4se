def _categorize(self, category):
    self.torrents = [result for result in self.torrents if result.category ==
        category]