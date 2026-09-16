def compareImage(self, body, plotShape='circle', imageScalar=2,
    imageEncoding='base64/png'):
    return self._image.getOverlayImage(self._retina, body, plotShape,
        imageScalar, imageEncoding)