def convert_thumbnail_to_pil(thumbnail, mode='RGB'):
    from PIL import Image
    if thumbnail.fmt == 0:
        size = thumbnail.width, thumbnail.height
        stride = thumbnail.widthbytes
        return Image.frombytes('RGBX', size, thumbnail.data, 'raw', mode,
            stride)
    elif thumbnail.fmt == 1:
        return Image.open(io.BytesIO(thumbnail.data))
    else:
        raise ValueError('Unknown thumbnail format %d' % thumbnail.fmt)