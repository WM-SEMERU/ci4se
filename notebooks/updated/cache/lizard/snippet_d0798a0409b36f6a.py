def height(self, container):
    height = float(self.get_style('font_size', container))
    script_level = self.script_level(container)
    if script_level > -1:
        height *= self.position_size * (5 / 6) ** script_level
    return height