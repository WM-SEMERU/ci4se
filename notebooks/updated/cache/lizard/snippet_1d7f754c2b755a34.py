def relStdDev(self, limit=None):
    moments = self.meanAndStdDev(limit)
    if moments is None:
        return None
    return moments[1] / moments[0]