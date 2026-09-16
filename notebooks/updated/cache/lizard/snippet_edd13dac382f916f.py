def dirty(self):
    return not os.path.exists(self.cachename) or os.path.getmtime(self.filename
        ) > os.path.getmtime(self.cachename)