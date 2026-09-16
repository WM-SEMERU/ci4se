def move(self, dst):
    shutil.move(self, dst)
    self = PathStr(dst).join(self.basename())
    return self