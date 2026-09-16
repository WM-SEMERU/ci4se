def _get_tags_by_num(self):
    by_revision = operator.attrgetter('revision')
    tags = sorted(self.get_tags(), key=by_revision)
    revision_tags = itertools.groupby(tags, key=by_revision)

    def get_id(rev):
        return rev.split(':', 1)[0]
    return dict((get_id(rev), [tr.tag for tr in tr_list]) for rev, tr_list in
        revision_tags)