def decorate(self, pos, widget, is_first=True):
    void = urwid.SolidFill(' ')
    line = None
    cols = []
    depth = self._tree.depth(pos)
    if depth > 0:
        cols.append((depth * self._indent, void)),
    iwidth, icon = self._construct_collapse_icon(pos)
    available_space = self._indent
    firstindent_width = self._icon_offset + iwidth
    if firstindent_width > available_space:
        raise NoSpaceError()
    is_leaf = self._tree.is_leaf(pos)
    if not is_leaf:
        if icon is not None:
            cols.append((available_space - firstindent_width, urwid.
                SolidFill(' ')))
            icon_pile = urwid.Pile([('pack', icon), void])
            cols.append((iwidth, icon_pile))
            available_space = self._icon_offset
        cols.append((available_space, urwid.SolidFill(' ')))
    else:
        cols.append((self._indent, urwid.SolidFill(' ')))
    cols.append(widget)
    line = urwid.Columns(cols, box_columns=range(len(cols))[:-1])
    return line