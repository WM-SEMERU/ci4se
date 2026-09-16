def project_versions(self, project):
    r_json = self._get_json('project/' + project + '/versions')
    versions = [Version(self._options, self._session, raw_ver_json) for
        raw_ver_json in r_json]
    return versions