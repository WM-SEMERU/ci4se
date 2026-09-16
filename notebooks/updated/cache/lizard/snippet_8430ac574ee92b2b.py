def render_word(self, word, size, color):
    pygame.font.init()
    font = pygame.font.Font(None, size)
    self.rendered_word = font.render(word, 0, color)
    self.word_size = font.size(word)