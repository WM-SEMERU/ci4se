def setSceneRect(self, *args):
    super(XNodeScene, self).setSceneRect(*args)
    self.setDirty()