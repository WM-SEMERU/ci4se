def tag(self):
    tag = self.m('getting git tags', cmdd=dict(cmd=
        'git tag -l --sort="version:refname"', cwd=self.local), verbose=False)
    if tag.get('returncode') == 0:
        return tag.get('stdout')