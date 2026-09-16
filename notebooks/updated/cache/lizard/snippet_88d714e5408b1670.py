def check_repo_teams(repo, allow_teams, deny_teams, team_names=None):
    assert isinstance(repo, github.Repository.Repository), type(repo)
    if not team_names:
        try:
            team_names = [t.name for t in repo.get_teams()]
        except github.RateLimitExceededException:
            raise
        except github.GithubException as e:
            msg = 'error getting teams'
            raise CaughtRepositoryError(repo, e, msg) from None
    if not any(x in team_names for x in allow_teams) or any(x in team_names for
        x in deny_teams):
        raise RepositoryTeamMembershipError(repo, team_names, allow_teams=
            allow_teams, deny_teams=deny_teams)