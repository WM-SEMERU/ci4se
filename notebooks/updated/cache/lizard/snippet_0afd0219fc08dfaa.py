def get_font_path(self):
    r = request.GetFontPath(display=self.display)
    return r.paths