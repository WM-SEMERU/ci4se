def push_git_package(self):
    self._pull_branch_from_origin()
    if self.deploy:
        self._write_commits_to_release_notes()
    try:
        self._write_new_tag_to_init()
        self._write_branch_and_tag_to_meta_yaml()
        self._push_new_tag_to_git()
    except Exception as inst:
        print('\n Error:\n', inst)
        self._revert_tag_in_init()
        sys.exit(2)