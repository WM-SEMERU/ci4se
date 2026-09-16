def isOnSiliconList(self, ra_deg, dec_deg, padding_pix=DEFAULT_PADDING):
    ch, col, row = self.getChannelColRowList(ra_deg, dec_deg)
    out = np.zeros(len(ch), dtype=bool)
    for channel in set(ch):
        mask = ch == channel
        if channel in self.brokenChannels:
            continue
        if channel > 84:
            continue
        out[mask] = self.colRowIsOnSciencePixelList(col[mask], row[mask],
            padding_pix)
    return out