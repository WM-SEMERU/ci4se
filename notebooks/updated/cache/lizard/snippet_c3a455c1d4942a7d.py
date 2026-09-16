def delete_notification_rule(self, id, **kwargs):
    endpoint = '{0}/{1}/notification_rules/{2}'.format(self.endpoint, self[
        'id'], id)
    return self.request('DELETE', endpoint=endpoint, query_params=kwargs)