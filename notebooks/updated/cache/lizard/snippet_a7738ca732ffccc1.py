def pg_ctl(self, cmd, *args, **kwargs):
    pg_ctl = [self._pgcommand('pg_ctl'), cmd]
    return subprocess.call(pg_ctl + ['-D', self._data_dir] + list(args), **
        kwargs) == 0