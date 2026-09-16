def enable_repositories(self, repositories):
    for r in repositories:
        if r['type'] != 'rhsm_channel':
            continue
        if r['name'] not in self.rhsm_channels:
            self.rhsm_channels.append(r['name'])
    if self.rhsm_active:
        subscription_cmd = (
            "subscription-manager repos '--disable=*' --enable=" +
            ' --enable='.join(self.rhsm_channels))
        self.run(subscription_cmd)
    repo_files = [r for r in repositories if r['type'] == 'yum_repo']
    for repo_file in repo_files:
        self.create_file(repo_file['dest'], repo_file['content'])
    packages = [r['name'] for r in repositories if r['type'] == 'package']
    if packages:
        self.yum_install(packages)