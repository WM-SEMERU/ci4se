def get_diff(self, rev1, rev2, path=None, ignore_whitespace=False, context=3):
    flags = ['-U%s' % context, '--full-index', '--binary', '-p', '-M',
        '--abbrev=40']
    if ignore_whitespace:
        flags.append('-w')
    if hasattr(rev1, 'raw_id'):
        rev1 = getattr(rev1, 'raw_id')
    if hasattr(rev2, 'raw_id'):
        rev2 = getattr(rev2, 'raw_id')
    if rev1 == self.EMPTY_CHANGESET:
        rev2 = self.get_changeset(rev2).raw_id
        cmd = ' '.join(['show'] + flags + [rev2])
    else:
        rev1 = self.get_changeset(rev1).raw_id
        rev2 = self.get_changeset(rev2).raw_id
        cmd = ' '.join(['diff'] + flags + [rev1, rev2])
    if path:
        cmd += ' -- "%s"' % path
    stdout, stderr = self.run_git_command(cmd)
    if rev1 == self.EMPTY_CHANGESET:
        lines = stdout.splitlines()
        x = 0
        for line in lines:
            if line.startswith('diff'):
                break
            x += 1
        stdout = '\n'.join(lines[x:]) + '\n'
    return stdout