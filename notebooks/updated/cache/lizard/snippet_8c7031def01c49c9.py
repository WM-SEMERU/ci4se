def set_naxispath(self, naxispath):
    revnaxis = list(naxispath)
    revnaxis.reverse()
    view = tuple(revnaxis + [slice(None), slice(None)])
    data = self.get_mddata()[view]
    if len(data.shape) != 2:
        raise ImageError('naxispath does not lead to a 2D slice: {}'.format
            (naxispath))
    self.naxispath = naxispath
    self.revnaxis = revnaxis
    self.set_data(data)