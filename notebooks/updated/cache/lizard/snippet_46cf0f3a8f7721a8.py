def search(self, href=None, query=None, query_fields=None, query_filter=
    None, limit=None, embed_items=None, embed_tracks=None, embed_metadata=
    None, embed_insights=None, language=None):
    assert query is not None
    assert limit is None or limit > 0
    if href is None:
        j = self._search_p1(query, query_fields, query_filter, limit,
            embed_items, embed_tracks, embed_metadata, embed_insights, language
            )
    else:
        j = self._search_pn(href, limit, embed_items, embed_tracks,
            embed_insights, embed_metadata)
    return self._parse_json(j)