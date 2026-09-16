def watermark(url, args=''):
    args = args.split(',')
    params = dict(name=args.pop(0), opacity=0.5, tile=False, scale=1.0,
        greyscale=False, rotation=0, position=None, quality=QUALITY,
        obscure=OBSCURE_ORIGINAL, random_position_once=RANDOM_POSITION_ONCE)
    params['url'] = unquote(url)
    for arg in args:
        key, value = arg.split('=')
        key, value = key.strip(), value.strip()
        if key == 'position':
            params['position'] = value
        elif key == 'opacity':
            params['opacity'] = utils._percent(value)
        elif key == 'tile':
            params['tile'] = bool(int(value))
        elif key == 'scale':
            params['scale'] = value
        elif key == 'greyscale':
            params['greyscale'] = bool(int(value))
        elif key == 'rotation':
            params['rotation'] = value
        elif key == 'quality':
            params['quality'] = int(value)
        elif key == 'obscure':
            params['obscure'] = bool(int(value))
        elif key == 'random_position_once':
            params['random_position_once'] = bool(int(value))
    return Watermarker()(**params)