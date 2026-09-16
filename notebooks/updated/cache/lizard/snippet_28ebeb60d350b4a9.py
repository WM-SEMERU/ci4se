def getContainerStats(self, limit=None, marker=None):
    stats = {}
    for row in self._conn.list_containers_info(limit, marker):
        stats[row['name']] = {'count': row['count'], 'size': row['bytes']}
    return stats