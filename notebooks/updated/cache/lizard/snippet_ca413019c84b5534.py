def delete_firmware_image(self, image_id):
    api = self._get_api(update_service.DefaultApi)
    api.firmware_image_destroy(image_id=image_id)
    return