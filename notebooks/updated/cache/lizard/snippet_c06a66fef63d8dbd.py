def load(self, draw_bbox=False, **kwargs):
    im = Image.new('RGBA', self.img_size)
    draw = None
    if draw_bbox:
        draw = ImageDraw.Draw(im)
    for sprite in self.images:
        data = sprite.load()
        sprite_im = Image.open(BytesIO(data))
        size = sprite.imgrect
        im.paste(sprite_im, (size[0], size[2]))
        if draw_bbox:
            draw.rectangle((size[0], size[2], size[1], size[3]), outline='red')
    del draw
    b = BytesIO()
    im.save(b, format='PNG')
    return b.getvalue()