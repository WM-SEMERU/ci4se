def focus_property(self, prop, direction):
    newpos = self.get_selected_mid()
    newpos = direction(newpos)
    while newpos is not None:
        MT = self._tree[newpos]
        if prop(MT):
            newpos = self._sanitize_position((newpos,))
            self.body.set_focus(newpos)
            break
        newpos = direction(newpos)