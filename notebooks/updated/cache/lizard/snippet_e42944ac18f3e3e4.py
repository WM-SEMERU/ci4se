def get_changelog(self, project, repository, ref_from, ref_to, limit=99999):
    url = ('rest/api/1.0/projects/{project}/repos/{repository}/compare/commits'
        .format(project=project, repository=repository))
    params = {}
    if ref_from:
        params['from'] = ref_from
    if ref_to:
        params['to'] = ref_to
    if limit:
        params['limit'] = limit
    return (self.get(url, params=params) or {}).get('values')