def cleanup_images(self, remove_old=False, keep_tags=None, **kwargs):
    self.push_log('Checking images for dependent images and containers.')
    set_raise_on_error(kwargs, False)
    return super(DockerFabricClient, self).cleanup_images(remove_old=
        remove_old, keep_tags=keep_tags, **kwargs)