def dragdrop(self, chviewer, uris):
    chname = self.get_channel_name(chviewer)
    self.open_uris(uris, chname=chname)
    return True