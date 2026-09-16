def color(self):
    return (self.tty_stream if self.options.color is None else self.options
        .color)