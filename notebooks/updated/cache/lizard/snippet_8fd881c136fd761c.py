def process(name, path, data, module=True):
    try:
        os.makedirs(path)
    except OSError:
        pass
    global font, glyph_data
    if font is None:
        font = ImageFont.truetype(FONT, FONT_SIZE * SCALE)
    if glyph_data is None:
        glyph_data = TTFont(font.path)
    if not isinstance(data, list):
        data = [data]
    if contains_bad_glyph(glyph_data, data):
        print('** %s has characters not in %s **' % (name, font.getname()[0]))
    else:
        create_screenshot(name, data, path, font=font, is_module=module)