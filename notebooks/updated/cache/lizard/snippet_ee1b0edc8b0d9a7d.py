def add_to_screen(self, screen_width, screen):
    for lineno, fields in enumerate(self.line_fields):
        for left, field in self.compute_positions(screen_width, fields):
            logger.debug('Adding field %s to screen %s at x=%d->%d, y=%d',
                field, screen.ref, left, left + field.width - 1, 1 + lineno)
            self.widgets[field] = field.add_to_screen(screen, left, 1 + lineno)
            self.register_hooks(field)