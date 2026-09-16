def rectangle(self, x1, y1, x2, y2, color='black', outline=False,
    outline_color='black'):
    return self.tk.create_rectangle(x1, y1, x2, y2, outline=utils.
        convert_color(outline_color) if outline else '', width=int(outline),
        fill='' if color is None else utils.convert_color(color))