def autocrop(im, autocrop=False, **kwargs):
    if autocrop:
        if utils.is_transparent(im):
            no_alpha = Image.new('L', im.size, 255)
            no_alpha.paste(im, mask=im.split()[-1])
        else:
            no_alpha = im.convert('L')
        bw = no_alpha.convert('L')
        bg = Image.new('L', im.size, 255)
        bbox = ImageChops.difference(bw, bg).getbbox()
        if bbox:
            im = im.crop(bbox)
    return im