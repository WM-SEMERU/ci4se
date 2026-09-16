def pictures(self):
    return [b for b in self.metadata_blocks if b.code == Picture.code]