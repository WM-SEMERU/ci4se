def clone_repo(pkg_name, repo_url):
    new_repo = ClonedRepo(name=pkg_name, origin=repo_url)
    new_repo.save()
    return new_repo