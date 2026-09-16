def collect_prs_info(self):
    REPO_RE = re.compile(
        '^(https://github.com/|git@github.com:)(?P<owner>.*?)/(?P<repo>.*?)(.git)?$'
        )
    PULL_RE = re.compile('^(refs/)?pull/(?P<pr>[0-9]+)/head$')
    remotes = {r['name']: r['url'] for r in self.remotes}
    all_prs = {}
    for merge in self.merges:
        remote = merge['remote']
        ref = merge['ref']
        repo_url = remotes[remote]
        repo_mo = REPO_RE.match(repo_url)
        if not repo_mo:
            logger.debug('%s is not a github repo', repo_url)
            continue
        pull_mo = PULL_RE.match(ref)
        if not pull_mo:
            logger.debug('%s is not a github pull reqeust', ref)
            continue
        pr_info = {'owner': repo_mo.group('owner'), 'repo': repo_mo.group(
            'repo'), 'pr': pull_mo.group('pr')}
        pr_info['path'] = '{owner}/{repo}/pulls/{pr}'.format(**pr_info)
        pr_info['url'] = 'https://github.com/{path}'.format(**pr_info)
        pr_info['shortcut'] = '{owner}/{repo}#{pr}'.format(**pr_info)
        r = self._github_api_get('/repos/{path}'.format(**pr_info))
        if r.status_code != 200:
            logger.warning(
                'Could not get status of {path}. Reason: {r.status_code} {r.reason}'
                .format(r=r, **pr_info))
            continue
        pr_info['state'] = r.json().get('state')
        pr_info['merged'] = (not r.json().get('merged') and 'not ' or ''
            ) + 'merged'
        all_prs.setdefault(pr_info['state'], []).append(pr_info)
    return all_prs