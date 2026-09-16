def delete_deps(self, conf, images):
    for dependency_name, _ in conf.dependency_images():
        image = images[dependency_name]
        if image.deleteable_image:
            log.info('Removing un-needed image {0}'.format(image.image_name))
            conf.harpoon.docker_api.remove_image(image.image_name)