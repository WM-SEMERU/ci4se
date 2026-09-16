def df(self, topic: str, parseNumbers=True):
    return util.df(self.extract(topic, parseNumbers))