def _construct_target_list(targets):
    target_entries = []
    for entry in targets:
        if not isinstance(entry, Gtk.TargetEntry):
            entry = Gtk.TargetEntry.new(*entry)
        target_entries.append(entry)
    return target_entries