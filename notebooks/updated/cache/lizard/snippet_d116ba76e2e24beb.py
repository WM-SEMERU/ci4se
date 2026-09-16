def getPlayAreaRect(self):
    fn = self.function_table.getPlayAreaRect
    rect = HmdQuad_t()
    result = fn(byref(rect))
    return result, rect