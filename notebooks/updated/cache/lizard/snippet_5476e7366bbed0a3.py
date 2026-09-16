def sky2pix_vec(self, pos, r, pa):
    ra, dec = pos
    x, y = self.sky2pix(pos)
    a = translate(ra, dec, r, pa)
    locations = self.sky2pix(a)
    x_off, y_off = locations
    a = np.sqrt((x - x_off) ** 2 + (y - y_off) ** 2)
    theta = np.degrees(np.arctan2(y_off - y, x_off - x))
    return x, y, a, theta