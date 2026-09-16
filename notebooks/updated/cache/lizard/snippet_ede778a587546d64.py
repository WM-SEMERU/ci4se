def get_opus_maximum_of(self, author_cts_urn):
    author = self.get_resource_by_urn(author_cts_urn)
    assert author is not None
    works = author.get_works()
    if len(works) > 1:
        for work in works:
            if work.is_opus_maximum():
                return work
    elif len(works) == 1:
        return works[0]
    else:
        return None