def topics(self):
    cluster = self._client.cluster
    if self._client._metadata_refresh_in_progress and self._client._topics:
        future = cluster.request_update()
        self._client.poll(future=future)
    stash = cluster.need_all_topic_metadata
    cluster.need_all_topic_metadata = True
    future = cluster.request_update()
    self._client.poll(future=future)
    cluster.need_all_topic_metadata = stash
    return cluster.topics()