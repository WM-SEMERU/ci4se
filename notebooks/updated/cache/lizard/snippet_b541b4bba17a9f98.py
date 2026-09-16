def create_git_tree(self, tree, base_tree=github.GithubObject.NotSet):
    assert all(isinstance(element, github.InputGitTreeElement) for element in
        tree), tree
    assert base_tree is github.GithubObject.NotSet or isinstance(base_tree,
        github.GitTree.GitTree), base_tree
    post_parameters = {'tree': [element._identity for element in tree]}
    if base_tree is not github.GithubObject.NotSet:
        post_parameters['base_tree'] = base_tree._identity
    headers, data = self._requester.requestJsonAndCheck('POST', self.url +
        '/git/trees', input=post_parameters)
    return github.GitTree.GitTree(self._requester, headers, data, completed
        =True)