def _image_attrs(self, attrs):
    path = None
    config = {**self._config}
    for key, val in attrs:
        if key.lower() == 'width' or key.lower() == 'height':
            try:
                config[key.lower()] = int(val)
            except ValueError:
                pass
        elif key.lower() == 'src':
            path = val
    img_path, img_args, _ = image.parse_image_spec(path)
    img = image.get_image(img_path, self._search_path)
    for key, val in img_args.items():
        if val and key not in config:
            config[key] = val
    try:
        img_attrs = img.get_img_attrs(**config)
    except FileNotFoundError as error:
        return [('data-publ-error', 'file not found: {}'.format(error.
            filename))]
    return [(key, val) for key, val in attrs if key.lower() not in img_attrs
        ] + list(img_attrs.items())