def default_campaign(campaign=None, expandcampvars=True, exclude_nodes=None,
    frozen=True):
    campaign = campaign or nameddict()

    def _merger(_camp, _deft):
        for key in _deft.keys():
            if key in _camp and isinstance(_camp[key], dict) and isinstance(
                _deft[key], collections.Mapping):
                _merger(_camp[key], _deft[key])
            elif key not in _camp:
                _camp[key] = _deft[key]
    _merger(campaign, DEFAULT_CAMPAIGN)
    campaign.setdefault('campaign_id', str(uuid.uuid4()))
    for precondition in campaign.precondition.keys():
        config = campaign.precondition[precondition]
        if not isinstance(config, list):
            campaign.precondition[precondition] = [config]

    def _expandvars(value):
        if isinstance(value, six.string_types):
            return expandvars(value)
        return value
    if expandcampvars:
        campaign = nameddict(dict_map_kv(campaign, _expandvars))
    else:
        campaign = nameddict(campaign)
    if expandcampvars:
        if campaign.network.get('tags') is None:
            campaign.network['tags'] = {}
        NetworkConfig(campaign).expand()
    return freeze(campaign) if frozen else campaign