def install_update_deps(self):
    logger.debug('')
    self._ctx.installed(self.name)
    depfile = os.path.join(self.repo_dir, '_upkg', 'depends')
    logger.debug('depfile? %s', depfile)
    if os.path.exists(depfile):
        logger.debug('Found depends file at %s', depfile)
        deps = open(depfile, 'r')
        dep = deps.readline()
        while dep:
            dep = dep.strip()
            logger.debug('depends: %s', dep)
            self._ctx.add_dep(nice_pkg_name(os.path.basename(dep)), dep)
            dep = deps.readline()
        deps.close()
    for rep in self._ctx.deps_needed:
        repo = Repo(url=rep)
        if repo.installed:
            repo.update()
        else:
            repo.install()