def add_scm_info(self):
    scm = get_scm()
    if scm:
        revision = scm.commit_id
        branch = scm.branch_name or revision
    else:
        revision, branch = 'none', 'none'
    self.add_infos(('revision', revision), ('branch', branch))