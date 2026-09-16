def delete_all_alerts_for(self, trigger):
    assert trigger is not None
    assert isinstance(trigger.id, str), 'Value must be a string'
    status, _ = self.http_client.delete(ALERTS_URI % trigger.id, params={
        'appid': self.API_key}, headers={'Content-Type': 'application/json'})