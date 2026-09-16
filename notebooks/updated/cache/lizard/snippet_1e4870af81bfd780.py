def read_feature(self, dataset, fid):
    uri = URITemplate(self.baseuri + '/{owner}/{did}/features/{fid}').expand(
        owner=self.username, did=dataset, fid=fid)
    return self.session.get(uri)