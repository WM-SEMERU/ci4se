def colorspace(im, bw=False, replace_alpha=False, **kwargs):
    if im.mode == 'I':
        im = im.point(list(_points_table()), 'L')
    is_transparent = utils.is_transparent(im)
    is_grayscale = im.mode in ('L', 'LA')
    new_mode = im.mode
    if is_grayscale or bw:
        new_mode = 'L'
    else:
        new_mode = 'RGB'
    if is_transparent:
        if replace_alpha:
            if im.mode != 'RGBA':
                im = im.convert('RGBA')
            base = Image.new('RGBA', im.size, replace_alpha)
            base.paste(im, mask=im)
            im = base
        else:
            new_mode = new_mode + 'A'
    if im.mode != new_mode:
        im = im.convert(new_mode)
    return im