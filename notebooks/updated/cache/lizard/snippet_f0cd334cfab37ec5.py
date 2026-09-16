def make_result(self):
    result = {}
    if self._base_image_build:
        result[BASE_IMAGE_KOJI_BUILD] = self._base_image_build
    if self._parent_builds:
        result[PARENT_IMAGES_KOJI_BUILDS] = self._parent_builds
    return result if result else None