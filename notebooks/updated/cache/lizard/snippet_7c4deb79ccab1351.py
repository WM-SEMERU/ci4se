def _run_tox_env(self, env_name, extra_env_vars={}):
    projdir = self.projdir
    env = deepcopy(os.environ)
    env['PATH'] = self._fixed_path(projdir)
    env.update(extra_env_vars)
    cmd = [os.path.join(projdir, 'bin', 'tox'), '-e', env_name]
    logger.info('Running tox environment %s: args="%s" cwd=%s timeout=1800',
        env_name, ' '.join(cmd), projdir)
    res = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.
        STDOUT, cwd=projdir, timeout=1800, env=env)
    logger.info('tox process exited %d', res.returncode)
    if res.returncode != 0:
        logger.error('ERROR: tox environment %s exitcode %d', env_name, res
            .returncode)
        logger.error('tox output:\n%s', res.stdout.decode())
        res.check_returncode()
    return res.stdout.decode()