def podcasts_iter(self, *, device_id=None, page_size=250):
    if device_id is None:
        device_id = self.device_id
    start_token = None
    prev_items = None
    while True:
        response = self._call(mc_calls.PodcastSeries, device_id,
            max_results=page_size, start_token=start_token)
        items = response.body.get('data', {}).get('items', [])
        if items != prev_items:
            subscribed_podcasts = [item for item in items if item.get(
                'userPreferences', {}).get('subscribed')]
            yield subscribed_podcasts
            prev_items = items
        else:
            break
        start_token = response.body.get('nextPageToken')
        if start_token is None:
            break