def have_thumbnail(self, fitsimage, image):
    chname = self.fv.get_channel_name(fitsimage)
    idx = image.get('idx', None)
    path = image.get('path', None)
    if path is not None:
        path = os.path.abspath(path)
        name = iohelper.name_image_from_path(path, idx=idx)
    else:
        name = 'NoName'
    name = image.get('name', name)
    thumbkey = self.get_thumb_key(chname, name, path)
    with self.thmblock:
        return thumbkey in self.thumb_dict