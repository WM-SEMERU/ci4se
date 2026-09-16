def put_image_layer(self, image_id, data):
    return self._http_call(self.IMAGE_JSON, put, data=data, image_id=image_id)