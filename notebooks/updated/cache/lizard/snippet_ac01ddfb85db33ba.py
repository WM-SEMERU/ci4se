def as_requirement(self):
    if isinstance(self.parsed_version, packaging.version.Version):
        spec = '%s==%s' % (self.project_name, self.parsed_version)
    else:
        spec = '%s===%s' % (self.project_name, self.parsed_version)
    return Requirement.parse(spec)