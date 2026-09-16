def default_icon_path(self):
    supported_exts = ['.png', '.svg']
    stripped = self.path.replace(os.path.join(self.load_path, 'assistants'), ''
        ).strip(os.sep)
    for ext in supported_exts:
        icon_with_ext = os.path.splitext(stripped)[0] + ext
        icon_fullpath = os.path.join(self.load_path, 'icons', icon_with_ext)
        if os.path.exists(icon_fullpath):
            return icon_fullpath
    return ''