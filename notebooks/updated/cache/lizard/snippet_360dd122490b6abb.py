def update_payload(self, fields=None):
    data = super(SyncPlan, self).update_payload(fields)
    if isinstance(data.get('sync_date'), datetime):
        data['sync_date'] = data['sync_date'].strftime('%Y-%m-%d %H:%M:%S')
    return data