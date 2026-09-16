def base_image_inspect(self):
    if self._base_image_inspect is None:
        if self.base_from_scratch:
            self._base_image_inspect = {}
        elif self.parents_pulled or self.custom_base_image:
            try:
                self._base_image_inspect = self.tasker.inspect_image(self.
                    base_image)
            except docker.errors.NotFound:
                raise KeyError(
                    'Unprocessed base image Dockerfile cannot be inspected')
        else:
            self._base_image_inspect = (atomic_reactor.util.
                get_inspect_for_image(self.base_image, self.base_image.
                registry, self.base_image_insecure, self.
                base_image_dockercfg_path))
        base_image_str = str(self.base_image)
        if base_image_str not in self._parent_images_inspect:
            self._parent_images_inspect[base_image_str
                ] = self._base_image_inspect
    return self._base_image_inspect