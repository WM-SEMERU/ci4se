def piece_size(self):
    if 'piece length' not in self.metainfo['info']:
        if self.size is None:
            return None
        else:
            self.calculate_piece_size()
    return self.metainfo['info']['piece length']