def sbo_version_source(self, slackbuilds):
    sbo_versions, sources = [], []
    for sbo in slackbuilds:
        status(0.02)
        sbo_ver = '{0}-{1}'.format(sbo, SBoGrep(sbo).version())
        sbo_versions.append(sbo_ver)
        sources.append(SBoGrep(sbo).source())
    return [sbo_versions, sources]