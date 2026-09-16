def image_import(self, image_name, url, image_meta, remote_host=None):
    try:
        self._imageops.image_import(image_name, url, image_meta,
            remote_host=remote_host)
    except exception.SDKBaseException:
        LOG.error("Failed to import image '%s'" % image_name)
        raise