def handle_padding(self, padding):
    left = padding[0]
    top = padding[1]
    right = padding[2]
    bottom = padding[3]
    offset_x = 0
    offset_y = 0
    new_width = self.engine.size[0]
    new_height = self.engine.size[1]
    if left > 0:
        offset_x = left
        new_width += left
    if top > 0:
        offset_y = top
        new_height += top
    if right > 0:
        new_width += right
    if bottom > 0:
        new_height += bottom
    new_engine = self.context.modules.engine.__class__(self.context)
    new_engine.image = new_engine.gen_image((new_width, new_height), '#fff')
    new_engine.enable_alpha()
    new_engine.paste(self.engine, (offset_x, offset_y))
    self.engine.image = new_engine.image