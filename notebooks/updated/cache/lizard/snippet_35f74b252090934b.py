def scale(self, image, geometry, upscale, crop):
    x_image, y_image = map(float, self.get_image_size(image))
    factors = geometry[0] / x_image, geometry[1] / y_image
    factor = max(factors) if crop else min(factors)
    if factor < 1 or upscale:
        width = toint(x_image * factor)
        height = toint(y_image * factor)
        image = self._scale(image, width, height)
    return image