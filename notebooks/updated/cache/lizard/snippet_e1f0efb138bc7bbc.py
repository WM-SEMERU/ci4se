def update(self):
    self.image = self.blank.copy()
    bf = self.font.render(''.join(self.text[:self.cursor_loc]), True, self.
        color)
    br = bf.get_rect().move(self.margin)
    af = self.font.render(''.join(self.text[self.cursor_loc:]), True, self.
        color)
    cr = self.cursor.get_rect()
    cvec = Vector(br.w - cr.w, 0) + self.margin
    scroll = Vector()
    if cvec.x > self.rect.w:
        scroll.x = self.rect.w - cvec.x - self.font.size(' ')[0]
    vcenter_blit(self.image, bf, scroll + br)
    vcenter_blit(self.image, af, scroll + br.topright)
    if self.cursor_shown and self.focus and pygame.key.get_focused():
        vcenter_blit(self.image, self.cursor, scroll + cvec)
    if self.blink_frames != None:
        self.blinker += 1
        self.blinker %= self.blink_frames
        if not self.blinker:
            self.cursor_shown = not self.cursor_shown