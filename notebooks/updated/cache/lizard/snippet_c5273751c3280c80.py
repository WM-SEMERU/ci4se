def add_picture(self, image_file, left, top, width=None, height=None):
    image_part, rId = self.part.get_or_add_image_part(image_file)
    pic = self._add_pic_from_image_part(image_part, rId, left, top, width,
        height)
    self._recalculate_extents()
    return self._shape_factory(pic)