def ProjectHomeRelative(self):
    return os.path.relpath(self.ProjectHome, os.path.dirname(self.FileName))