def add_path(self, path):
    abspath = os.path.abspath(path)
    self.children.append(_build_project_tree(abspath, self.followsymlinks,
        self.file_filter))