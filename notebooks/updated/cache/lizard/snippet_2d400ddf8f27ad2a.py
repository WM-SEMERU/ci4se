def _get_upstream(self):
    if not self._remote or not self._branch:
        branch = self.branch_name
        if not branch:
            raise Scm.LocalException('Failed to determine local branch')

        def get_local_config(key):
            value = self._check_output(['config', '--local', '--get', key],
                raise_type=Scm.LocalException)
            return value.strip()
        self._remote = self._remote or get_local_config('branch.{}.remote'.
            format(branch))
        self._branch = self._branch or get_local_config('branch.{}.merge'.
            format(branch))
    return self._remote, self._branch