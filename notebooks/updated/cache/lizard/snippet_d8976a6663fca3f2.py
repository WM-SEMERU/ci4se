def _identify(self, dataframe):
    id1 = dataframe[self.channels[0]] >= self.vert[0]
    id2 = dataframe[self.channels[1]] >= self.vert[1]
    if 'left' in self.region:
        id1 = ~id1
    if 'bottom' in self.region:
        id2 = ~id2
    idx = id1 & id2
    if 'out' in self.region:
        idx = ~idx
    return idx