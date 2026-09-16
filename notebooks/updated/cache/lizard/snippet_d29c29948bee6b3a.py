def have_active_commit(self):
    commit_state = sfs.file_or_default(sfs.cpjoin(self.base_path,
        'active_commit'), None)
    if commit_state != None:
        return True
    return False