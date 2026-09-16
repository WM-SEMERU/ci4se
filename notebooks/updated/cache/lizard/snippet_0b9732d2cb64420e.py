def diff(self, diff):
    if diff is None:
        return None
    return dict(toVol=diff.toUUID, fromVol=diff.fromUUID, size=diff.size,
        sizeIsEstimated=diff.sizeIsEstimated)