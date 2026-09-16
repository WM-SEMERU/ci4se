def update_highlights(self, old_highlight_set, new_highlight_set):
    with self.thmblock:
        un_hilite_set = old_highlight_set - new_highlight_set
        re_hilite_set = new_highlight_set - old_highlight_set
        bg = self.settings.get('label_bg_color', 'lightgreen')
        fg = self.settings.get('label_font_color', 'black')
        for thumbkey in un_hilite_set:
            if thumbkey in self.thumb_dict:
                namelbl = self.thumb_dict[thumbkey].get('namelbl')
                namelbl.color = fg
        for thumbkey in re_hilite_set:
            if thumbkey in self.thumb_dict:
                namelbl = self.thumb_dict[thumbkey].get('namelbl')
                namelbl.color = bg
    if self.gui_up:
        self.c_view.redraw(whence=3)