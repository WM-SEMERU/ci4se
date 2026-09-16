def results(self, campaign_id):
    return super(API, self).get(resource_id=campaign_id, resource_action=
        'results', resource_cls=CampaignResults)