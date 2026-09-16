def _recurse(self, parent, dir_included=False):
    try:
        children = parent.enumerate_children(Gio.
            FILE_ATTRIBUTE_STANDARD_NAME, Gio.FileQueryInfoFlags.
            NOFOLLOW_SYMLINKS, None)
    except GLib.GError:
        yield parent
        return
    for child in children:
        name = child.get_name()
        child = parent.get_child(name)
        try:
            for sub in self._recurse(child):
                yield sub
        except GLib.GError:
            yield child
    if dir_included:
        yield parent