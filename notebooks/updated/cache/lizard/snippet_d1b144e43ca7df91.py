def parent_image_inspect(self, image):
    image_name = ImageName.parse(image)
    if image_name not in self._parent_images_inspect:
        if self.parents_pulled:
            self._parent_images_inspect[image_name
                ] = self.tasker.inspect_image(image)
        else:
            self._parent_images_inspect[image_name
                ] = atomic_reactor.util.get_inspect_for_image(image_name,
                image_name.registry, self.base_image_insecure, self.
                base_image_dockercfg_path)
    return self._parent_images_inspect[image_name]