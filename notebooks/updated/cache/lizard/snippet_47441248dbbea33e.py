def get_relation_graph(self, depth=None):
    url = '{}relation_graph/'.format(self.url)
    if depth is not None:
        params = {'depth': depth}
    else:
        params = {}
    from .sample_relation import SampleRelation
    return SampleRelation._get_iter_from_url(url, params=params,
        append_base_url=False)