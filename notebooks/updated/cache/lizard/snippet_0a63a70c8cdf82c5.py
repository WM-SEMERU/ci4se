def _get_message(self, key, since=None):
    stored = self.store[key]
    if isinstance(stored, dict):
        filename = stored['path']
        folder = stored['folder']
        if since and since > 0.0:
            st = stat(filename)
            if st.st_mtime < since:
                return None
        stored = MdMessage(key, filename=filename, folder=folder,
            filesystem=folder.filesystem)
        self.store[key] = stored
    elif since and since > 0.0:
        st = stat(stored.filename)
        if st.st_mtime < since:
            return None
    return stored