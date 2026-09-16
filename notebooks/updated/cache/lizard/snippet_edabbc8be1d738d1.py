def _get_images(self):
    self._init_os_api()
    try:
        return self.nova_client.images.list()
    except AttributeError:
        return list(self.glance_client.images.list())