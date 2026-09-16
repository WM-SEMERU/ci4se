def uninstall(self, pkgname, *args, **kwargs):
    auto_confirm = kwargs.pop('auto_confirm', True)
    verbose = kwargs.pop('verbose', False)
    with self.activated():
        monkey_patch = next(iter(dist for dist in self.base_working_set if 
            dist.project_name == 'recursive-monkey-patch'), None)
        if monkey_patch:
            monkey_patch.activate()
        pip_shims = self.safe_import('pip_shims')
        pathset_base = pip_shims.UninstallPathSet
        pathset_base._permitted = PatchedUninstaller._permitted
        dist = next(iter(filter(lambda d: d.project_name == pkgname, self.
            get_working_set())), None)
        pathset = pathset_base.from_dist(dist)
        if pathset is not None:
            pathset.remove(auto_confirm=auto_confirm, verbose=verbose)
        try:
            yield pathset
        except Exception as e:
            if pathset is not None:
                pathset.rollback()
        else:
            if pathset is not None:
                pathset.commit()
        if pathset is None:
            return