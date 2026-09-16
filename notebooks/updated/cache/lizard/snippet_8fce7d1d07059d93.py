def get_darktime(self, img):
    header = self.get_header(img)
    if 'DARKTIME' in header.keys():
        return header['DARKTIME']
    else:
        return self.get_exptime(img)