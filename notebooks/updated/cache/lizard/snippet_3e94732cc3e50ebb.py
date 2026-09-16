def set_maskalpha(self):
    try:
        a = float(self.w.mask_alpha.get_text())
    except ValueError:
        self.logger.error('Cannot set mask alpha')
        self.w.mask_alpha.set_text(str(self.maskalpha))
        return
    if a < 0 or a > 1:
        self.logger.error('Alpha must be between 0 and 1, inclusive')
        self.w.mask_alpha.set_text(str(self.maskalpha))
        return
    self.maskalpha = a