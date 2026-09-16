def resize_program_image(img_url, img_size=300):
    match = re.match('.+/(\\d+)x(\\d+)/.+', img_url)
    if not match:
        _LOGGER.warning('Could not compute current image resolution of %s',
            img_url)
        return img_url
    res_x = int(match.group(1))
    res_y = int(match.group(2))
    target_res_y = int(img_size * res_y / res_x)
    return re.sub('{}x{}'.format(res_x, res_y), '{}x{}'.format(img_size,
        target_res_y), img_url)