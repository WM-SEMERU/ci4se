def iter_entry_points(self, group, name=None):
    return (entry for dist in self for entry in dist.get_entry_map(group).
        values() if name is None or name == entry.name)