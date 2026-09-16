def get_trending_daily_not_starred(self):
    trending_daily = self.get_trending_daily()
    starred_repos = self.get_starred_repos()
    repos_list = []
    for repo in trending_daily:
        if repo not in starred_repos:
            repos_list.append(repo)
    return repos_list