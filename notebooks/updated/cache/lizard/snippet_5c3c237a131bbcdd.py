def image_postprocess(imagefile, output, size, crop, render):
    try:
        from PIL import Image
    except ImportError:
        import Image
    img = Image.open(imagefile)
    size_crop = None
    img_resized = img
    if size and crop and crop.lower() == 'true':
        width_raw, height_raw = img.size
        width, height = size
        height_better = int(height_raw * (float(width) / width_raw))
        if height < height_better:
            size_crop = 0, 0, width, height
    try:
        if size_crop:
            size_better = width, height_better
            img_better = img.resize(size_better, Image.ANTIALIAS)
            img_resized = img_better.crop(size_crop)
        elif size:
            img_resized = img.resize(size, Image.ANTIALIAS)
        if render == 'bmp':
            img_resized = img_resized.convert('RGB')
        elif render == 'xbm':
            img_resized = img_resized.convert('1')
        img_resized.save(output, render)
    except KeyError:
        raise UnsupportedImageFormat
    except IOError as e:
        raise CaptureError(e)