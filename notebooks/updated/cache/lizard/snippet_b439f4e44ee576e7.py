def add_crosshair_to_image(fname, opFilename):
    im = Image.open(fname)
    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=(255, 255, 255))
    draw.line((0, im.size[1], im.size[0], 0), fill=(255, 255, 255))
    del draw
    im.save(opFilename)