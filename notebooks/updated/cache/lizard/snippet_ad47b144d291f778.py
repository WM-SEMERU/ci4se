def set_bracket_matcher_color_scheme(self, color_scheme):
    bsh = sh.BaseSH(parent=self, color_scheme=color_scheme)
    mpcolor = bsh.get_matched_p_color()
    self._bracket_matcher.format.setBackground(mpcolor)