def commits(self, branch, since=0, to=int(time.time()) + 86400):
    since_str = datetime.datetime.fromtimestamp(since).strftime('%Y-%m-%d')
    to_str = datetime.datetime.fromtimestamp(to).strftime('%Y-%m-%d')
    commits = {}
    req_message = ('https://api.bitbucket.org/2.0/repositories/' + self.
        reponame + '/commits/' + branch)
    loop_continue = True
    while loop_continue:
        response_data = self._bitbucketAPIRequest(req_message)
        for commit in response_data['values']:
            if commit['date'] < since_str:
                loop_continue = False
                break
            elif commit['date'] > to_str:
                continue
            else:
                commits[commit['hash']] = self._commitData(commit)
        if 'next' not in response_data:
            break
        req_message = response_data['next']
    return commits