def getPoints(self, pared=False):
    points = self._points[:]
    if pared:
        np = NodePare()
        np.addPoints(points)
        np.parePoints()
        points = np.getParedPoints()
    return points