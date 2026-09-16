def saveShx(self, target):
    if not hasattr(target, 'write'):
        target = os.path.splitext(target)[0] + '.shx'
    if not self.shapeType:
        self.shapeType = self._shapes[0].shapeType
    self.shx = self.__getFileObj(target)
    self.__shapefileHeader(self.shx, headerType='shx')
    self.__shxRecords()