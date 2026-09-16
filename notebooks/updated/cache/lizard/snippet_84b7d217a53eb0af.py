def find_revision_number(self, revision=None):
    self.create()
    revision = revision or self.default_revision
    output = self.context.capture('hg', 'id', '--rev=%s' % revision, '--num'
        ).rstrip('+')
    if not output.isdigit():
        msg = (
            "Failed to find local revision number! ('hg id --num' gave unexpected output)"
            )
        raise EnvironmentError(msg)
    return int(output)