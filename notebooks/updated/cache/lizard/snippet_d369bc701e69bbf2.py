def draw_character_key(self, surface, key, special=False):
    background_color = self.key_background_color
    if special and self.special_key_background_color is not None:
        background_color = self.special_key_background_color
    pygame.draw.rect(surface, background_color[key.state], key.position +
        key.size)
    size = self.font.size(key.value)
    x = key.position[0] + (key.size[0] - size[0]) / 2
    y = key.position[1] + (key.size[1] - size[1]) / 2
    surface.blit(self.font.render(key.value, 1, self.text_color[key.state],
        None), (x, y))