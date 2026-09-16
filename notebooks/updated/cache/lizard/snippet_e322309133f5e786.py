def _isConfigFile(self, filename):
    ext = os.path.splitext(filename)[1].lower()
    if filename in self.FB_CONFIG_FILES:
        return True
    elif ext in self.FB_META_EXTENSIONS:
        return True
    return False