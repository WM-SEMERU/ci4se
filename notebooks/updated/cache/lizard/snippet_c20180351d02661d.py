def push(self, repository=None, tag=None):
    image = self
    if repository or tag:
        image = self.tag_image(repository, tag)
    for json_e in self.d.push(repository=image.name, tag=image.tag, stream=
        True, decode=True):
        logger.debug(json_e)
        status = graceful_get(json_e, 'status')
        if status:
            logger.info(status)
        else:
            error = graceful_get(json_e, 'error')
            if error is not None:
                logger.error(status)
                raise ConuException(
                    'There was an error while pushing the image %s: %s',
                    self.name, error)
    return image