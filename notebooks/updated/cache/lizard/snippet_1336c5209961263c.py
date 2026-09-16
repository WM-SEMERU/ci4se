def update_vcs(self, fname, index):
    fpath = os.path.dirname(fname)
    branches, branch, files_modified = get_git_refs(fpath)
    text = branch if branch else ''
    if len(files_modified):
        text = text + ' [{}]'.format(len(files_modified))
    self.setVisible(bool(branch))
    self.set_value(text)