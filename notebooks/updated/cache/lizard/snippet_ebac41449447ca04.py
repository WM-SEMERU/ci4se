def topics(self, exclude_internal_topics=True):
    topics = set(self._partitions.keys())
    if exclude_internal_topics:
        return topics - self.internal_topics
    else:
        return topics