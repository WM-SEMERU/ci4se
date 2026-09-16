def images_grouped_by_type(self):
    type = -1
    images = []
    for wc in self:
        if wc.type != type:
            if images:
                yield type, images
            role = wc.role
            creators = []
            images.append(wc.image)
    if images:
        yield type, images