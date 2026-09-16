def horizontal_border(self, style, outer_widths):
    if style == 'top':
        horizontal = self.CHAR_OUTER_TOP_HORIZONTAL
        left = self.CHAR_OUTER_TOP_LEFT
        intersect = (self.CHAR_OUTER_TOP_INTERSECT if self.
            inner_column_border else '')
        right = self.CHAR_OUTER_TOP_RIGHT
        title = self.title
    elif style == 'bottom':
        horizontal = self.CHAR_OUTER_BOTTOM_HORIZONTAL
        left = self.CHAR_OUTER_BOTTOM_LEFT
        intersect = (self.CHAR_OUTER_BOTTOM_INTERSECT if self.
            inner_column_border else '')
        right = self.CHAR_OUTER_BOTTOM_RIGHT
        title = None
    elif style == 'heading':
        horizontal = self.CHAR_H_INNER_HORIZONTAL
        left = self.CHAR_H_OUTER_LEFT_INTERSECT if self.outer_border else ''
        intersect = (self.CHAR_H_INNER_INTERSECT if self.
            inner_column_border else '')
        right = self.CHAR_H_OUTER_RIGHT_INTERSECT if self.outer_border else ''
        title = None
    elif style == 'footing':
        horizontal = self.CHAR_F_INNER_HORIZONTAL
        left = self.CHAR_F_OUTER_LEFT_INTERSECT if self.outer_border else ''
        intersect = (self.CHAR_F_INNER_INTERSECT if self.
            inner_column_border else '')
        right = self.CHAR_F_OUTER_RIGHT_INTERSECT if self.outer_border else ''
        title = None
    else:
        horizontal = self.CHAR_INNER_HORIZONTAL
        left = self.CHAR_OUTER_LEFT_INTERSECT if self.outer_border else ''
        intersect = (self.CHAR_INNER_INTERSECT if self.inner_column_border else
            '')
        right = self.CHAR_OUTER_RIGHT_INTERSECT if self.outer_border else ''
        title = None
    return build_border(outer_widths, horizontal, left, intersect, right, title
        )