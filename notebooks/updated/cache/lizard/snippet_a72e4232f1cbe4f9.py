def move(self, group, cluster_ids=None):
    if isinstance(cluster_ids, string_types):
        logger.warn(
            'The list of clusters should be a list of integers, not a string.')
        return
    self.label('group', group, cluster_ids=cluster_ids)