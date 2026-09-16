def wa(self, chamber):
    if isinstance(chamber, int):
        chamber = str(chamber)
    return WorldAssembly(chamber, self)