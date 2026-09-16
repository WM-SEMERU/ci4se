def getScreenDims(self):
    width = ale_lib.getScreenWidth(self.obj)
    height = ale_lib.getScreenHeight(self.obj)
    return width, height