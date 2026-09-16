def remove(self, flag, extra):
    self.flag = flag
    self.extra = extra
    self.dep_path = self.meta.log_path + 'dep/'
    dependencies, rmv_list = [], []
    self.removed = self._view_removed()
    if not self.removed:
        print('')
    else:
        msg = 'package'
        if len(self.removed) > 1:
            msg = msg + 's'
        try:
            if self.meta.default_answer in ['y', 'Y']:
                remove_pkg = self.meta.default_answer
            else:
                remove_pkg = raw_input(
                    '\nAre you sure to remove {0} {1} [y/N]? '.format(str(
                    len(self.removed)), msg))
        except EOFError:
            print('')
            raise SystemExit()
        if remove_pkg in ['y', 'Y']:
            self._check_if_used(self.binary)
            for rmv in self.removed:
                if os.path.isfile(self.dep_path + rmv
                    ) and self.meta.del_deps in ['on', 'ON'] or os.path.isfile(
                    self.dep_path + rmv) and '--deps' in self.extra:
                    dependencies = self._view_deps(self.dep_path, rmv)
                    if dependencies and self._rmv_deps_answer() in ['y', 'Y']:
                        rmv_list += self._rmv_deps(dependencies, rmv)
                    else:
                        rmv_list += self._rmv_pkg(rmv)
                else:
                    rmv_list += self._rmv_pkg(rmv)
            self._reference_rmvs(rmv_list)