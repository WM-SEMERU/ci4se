def left_margin(self, margin):
    if margin <= 255 and margin >= 0:
        self.send(chr(27) + 'I' + chr(margin))
    else:
        raise RuntimeError('Invalid margin parameter.')