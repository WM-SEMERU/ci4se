def get_or_add_image_part(self, image_file):
    image_part = self._package.get_or_add_image_part(image_file)
    rId = self.relate_to(image_part, RT.IMAGE)
    return image_part, rId