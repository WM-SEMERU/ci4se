def _cmd(self, *nargs):
    cmd_str = ' '.join(map(quote, nargs))
    if self.package.config.debug('package_release'):
        print_debug('Running command: %s' % cmd_str)
    p = popen(nargs, stdout=subprocess.PIPE, stderr=subprocess.PIPE, cwd=
        self.pkg_root)
    out, err = p.communicate()
    if p.returncode:
        print_debug('command stdout:')
        print_debug(out)
        print_debug('command stderr:')
        print_debug(err)
        raise ReleaseVCSError('command failed: %s\n%s' % (cmd_str, err))
    out = out.strip()
    if out:
        return [x.rstrip() for x in out.split('\n')]
    else:
        return []