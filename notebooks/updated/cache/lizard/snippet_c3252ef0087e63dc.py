def build_image_from_path(self, path, image, use_cache=False, remove_im=True):
    logger.info("building image '%s' from path '%s'", image, path)
    response = self.d.build(path=path, tag=image.to_str(), nocache=not
        use_cache, decode=True, rm=remove_im, forcerm=True, pull=False)
    return response