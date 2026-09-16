def commit_container(self, container_id, image=None, message=None):
    logger.info("committing container '%s'", container_id)
    logger.debug("container_id = '%s', image = '%s', message = '%s'",
        container_id, image, message)
    tag = None
    if image:
        tag = image.tag
        image = image.to_str(tag=False)
    response = self.d.commit(container_id, repository=image, tag=tag,
        message=message)
    logger.debug("response = '%s'", response)
    try:
        return response['Id']
    except KeyError:
        logger.error('ID missing from commit response')
        raise RuntimeError('ID missing from commit response')