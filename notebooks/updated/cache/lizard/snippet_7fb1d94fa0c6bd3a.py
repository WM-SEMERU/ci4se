def put_images_layer(self, image_id, data):
    return self._http_call(self.IMAGE_LAYER, put, image_id=image_id, data=data)