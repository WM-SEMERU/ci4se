def _image_url(array, fmt='png', mode='data', quality=90, domain=None):
    supported_modes = 'data'
    if mode not in supported_modes:
        message = "Unsupported mode '%s', should be one of '%s'."
        raise ValueError(message, mode, supported_modes)
    image_data = serialize_array(array, fmt=fmt, quality=quality)
    base64_byte_string = base64.b64encode(image_data).decode('ascii')
    return 'data:image/' + fmt.upper() + ';base64,' + base64_byte_string