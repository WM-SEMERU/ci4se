def isOnSilicon(self, ra_deg, dec_deg, padding_pix=DEFAULT_PADDING):
    ch, col, row = self.getChannelColRow(ra_deg, dec_deg)
    if ch in self.brokenChannels:
        return False
    if ch > 84:
        return False
    return self.colRowIsOnSciencePixel(col, row, padding_pix)