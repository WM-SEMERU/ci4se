def add_image_info_cb(self, viewer, channel, image_info):
    chname = channel.name
    name = image_info.name
    self.logger.debug('name=%s' % name)
    try:
        image = channel.get_loaded_image(name)
    except KeyError:
        image = None
    self.add_image_cb(viewer, chname, image, image_info)