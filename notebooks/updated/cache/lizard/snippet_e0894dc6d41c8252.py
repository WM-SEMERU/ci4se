def create_tag(self, tag_name=None, **properties):
    tag = Gtk.TextTag(name=tag_name, **properties)
    self._get_or_create_tag_table().add(tag)
    return tag