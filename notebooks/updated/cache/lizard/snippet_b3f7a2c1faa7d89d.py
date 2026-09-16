def find_revision_id(self, revision=None):
    self.create()
    revision = self.expand_branch_name(revision)
    output = self.context.capture('git', 'rev-parse', revision)
    return self.ensure_hexadecimal_string(output, 'git rev-parse')