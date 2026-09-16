def SearchFetchable(session=None, **kwargs):
    session = session or Session.login()
    return util.Fetchable.fetch_marshall(SearchHTMLFetcher(session, **
        kwargs), util.SimpleProcessor(session, lambda match_card_div:
        Profile(session=session, **MatchCardExtractor(match_card_div).
        as_dict), _match_card_xpb))