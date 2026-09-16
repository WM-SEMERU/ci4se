def GetAdGroups(self, client_customer_id, campaign_id):
    self.client.SetClientCustomerId(client_customer_id)
    selector = {'fields': ['Id', 'Name', 'Status'], 'predicates': [{'field':
        'CampaignId', 'operator': 'EQUALS', 'values': [campaign_id]}, {
        'field': 'Status', 'operator': 'NOT_EQUALS', 'values': ['REMOVED']}]}
    adgroups = self.client.GetService('AdGroupService').get(selector)
    if int(adgroups['totalNumEntries']) > 0:
        return adgroups['entries']
    else:
        return None