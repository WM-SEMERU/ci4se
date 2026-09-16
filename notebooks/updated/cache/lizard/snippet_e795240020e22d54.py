def get_iex_corporate_actions(start=None, **kwargs):
    import warnings
    warnings.warn(WNG_MSG % ('get_iex_corporate_actions',
        'refdata.get_iex_corporate_actions'))
    return CorporateActions(start=start, **kwargs).fetch()