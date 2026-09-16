def remove_device(self, device, id_override=None, type_override=None):
    object_id = id_override or device.object_id()
    object_type = type_override or device.object_type()
    url_string = '{}/{}s/{}'.format(self.BASE_URL, object_type, object_id)
    try:
        arequest = requests.delete(url_string, headers=API_HEADERS)
        if arequest.status_code == 204:
            return True
        _LOGGER.error('Failed to remove device. Status code: %s', arequest.
            status_code)
        return False
    except requests.exceptions.RequestException:
        _LOGGER.error('Failed to remove device.')
        return False