def folderitem(self, obj, item, index):
    obj = api.get_object(obj)
    url = '{}/analysisrequests'.format(api.get_url(obj))
    bid = api.get_id(obj)
    cbid = obj.getClientBatchID()
    title = api.get_title(obj)
    client = obj.getClient()
    created = api.get_creation_date(obj)
    date = obj.getBatchDate()
    item['BatchID'] = bid
    item['ClientBatchID'] = cbid
    item['replace']['BatchID'] = get_link(url, bid)
    item['Title'] = title
    item['replace']['Title'] = get_link(url, title)
    item['created'] = self.ulocalized_time(created, long_format=True)
    item['BatchDate'] = self.ulocalized_time(date, long_format=True)
    if client:
        client_url = api.get_url(client)
        client_name = client.getName()
        client_id = client.getClientID()
        item['Client'] = client_name
        item['ClientID'] = client_id
        item['replace']['Client'] = get_link(client_url, client_name)
        item['replace']['ClientID'] = get_link(client_url, client_id)
    return item