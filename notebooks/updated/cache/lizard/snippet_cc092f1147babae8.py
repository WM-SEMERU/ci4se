def image(self):
    slide_part, rId = self.part, self._element.blip_rId
    if rId is None:
        raise ValueError('no embedded image')
    return slide_part.get_image(rId)