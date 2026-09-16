def delete_trigger_events(self, trigger_id, event_ids):
    response = self._client.session.delete('{url}/{trigger_id}/events/delete'
        .format(url=self.endpoint_url, trigger_id=trigger_id), params={
        'events': event_ids})
    return self.process_response(response)