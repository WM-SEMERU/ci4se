def get_imgid(self, img):
    imgid = img.filename()
    hdr = self.get_header(img)
    if 'checksum' in hdr:
        return hdr['checksum']
    if 'filename' in hdr:
        return hdr['filename']
    if not imgid:
        imgid = repr(img)
    return imgid