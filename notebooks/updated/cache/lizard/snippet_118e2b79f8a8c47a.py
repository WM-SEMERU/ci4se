def tag_and_push_image(self, image, target_image, insecure=False, force=
    False, dockercfg=None):
    logger.info("tagging and pushing image '%s' as '%s'", image, target_image)
    logger.debug("image = '%s', target_image = '%s'", image, target_image)
    self.tag_image(image, target_image, force=force)
    if dockercfg:
        self.login(registry=target_image.registry, docker_secret_path=dockercfg
            )
    return self.push_image(target_image, insecure=insecure)