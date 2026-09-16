def _menuitem(self, label, icon, onclick, checked=None):
    if checked is not None:
        item = Gtk.CheckMenuItem()
        item.set_active(checked)
    elif icon is None:
        item = Gtk.MenuItem()
    else:
        item = Gtk.ImageMenuItem()
        item.set_image(icon)
        item.set_always_show_image(True)
    if label is not None:
        item.set_label(label)
    if isinstance(onclick, Gtk.Menu):
        item.set_submenu(onclick)
    elif onclick is not None:
        item.connect('activate', onclick)
    return item