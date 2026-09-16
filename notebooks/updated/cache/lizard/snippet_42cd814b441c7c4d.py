def image_to_url(image, colormap=None, origin='upper'):
    if isinstance(image, str) and not _is_url(image):
        fileformat = os.path.splitext(image)[-1][1:]
        with io.open(image, 'rb') as f:
            img = f.read()
        b64encoded = base64.b64encode(img).decode('utf-8')
        url = 'data:image/{};base64,{}'.format(fileformat, b64encoded)
    elif 'ndarray' in image.__class__.__name__:
        img = write_png(image, origin=origin, colormap=colormap)
        b64encoded = base64.b64encode(img).decode('utf-8')
        url = 'data:image/png;base64,{}'.format(b64encoded)
    else:
        url = json.loads(json.dumps(image))
    return url.replace('\n', ' ')