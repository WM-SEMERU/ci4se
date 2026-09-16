def _Publish(campaign, subcampaign, strkwargs):
    kwargs = pickle.loads(strkwargs.replace('%%%', '\n').encode('utf-8'))
    cadence = kwargs.get('cadence', 'lc')
    m = FunctionWrapper(EverestModel, season=campaign, publish=True, **kwargs)
    sys.excepthook = ExceptionHook
    with Pool() as pool:
        if subcampaign != -1:
            campaign = campaign + 0.1 * subcampaign
        stars = GetK2Campaign(campaign, epics_only=True, cadence=cadence)
        pool.map(m, stars)