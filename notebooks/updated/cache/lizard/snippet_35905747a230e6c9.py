def parse(self, data, length, version=1):
    pos = data.tell()
    self.characterId = data.readUI16()
    self.depth = data.readUI16()
    self.matrix = data.readMATRIX()
    self.hasCharacter = True
    self.hasMatrix = True
    if data.tell() - pos < length:
        colorTransform = data.readCXFORM()
        self.hasColorTransform = True