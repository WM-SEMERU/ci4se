def _checkMousePositionForFocus(self):
    i = 0
    cur_pos = pygame.mouse.get_pos()
    ml, mt = self.position
    for o in self.options:
        rect = o.get('label_rect')
        if rect:
            if rect.collidepoint(cur_pos) and self.mouse_pos != cur_pos:
                self.option = i
                self.mouse_pos = cur_pos
                break
        i += 1