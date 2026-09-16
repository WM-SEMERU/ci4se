def create_card(self, note=github.GithubObject.NotSet, content_id=github.
    GithubObject.NotSet, content_type=github.GithubObject.NotSet):
    post_parameters = {}
    if isinstance(note, (str, unicode)):
        assert content_id is github.GithubObject.NotSet, content_id
        assert content_type is github.GithubObject.NotSet, content_type
        post_parameters = {'note': note}
    else:
        assert note is github.GithubObject.NotSet, note
        assert isinstance(content_id, int), content_id
        assert isinstance(content_type, (str, unicode)), content_type
        post_parameters = {'content_id': content_id, 'content_type':
            content_type}
    import_header = {'Accept': Consts.mediaTypeProjectsPreview}
    headers, data = self._requester.requestJsonAndCheck('POST', self.url +
        '/cards', headers=import_header, input=post_parameters)
    return github.ProjectCard.ProjectCard(self._requester, headers, data,
        completed=True)