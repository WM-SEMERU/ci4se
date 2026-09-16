def image_exists(self, image_name, tag='latest'):
    code, image = self.image_tags(image_name)
    if code != httplib.OK:
        return False
    tag = tag.lower()
    return any(x.lower() == tag for x in image.tags)