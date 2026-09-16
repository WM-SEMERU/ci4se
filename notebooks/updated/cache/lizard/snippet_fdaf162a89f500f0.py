def setSceneRect(self, *args):
    super(XChartScene, self).setSceneRect(*args)
    self._dirty = True