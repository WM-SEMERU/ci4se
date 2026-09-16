def get_selected_tag(self):
    cols, _ = self.taglist.get_focus()
    tagwidget = cols.original_widget.get_focus()
    return tagwidget.tag