def get_screen_size_range(self):
    return GetScreenSizeRange(display=self.display, opcode=self.display.
        get_extension_major(extname), window=self)