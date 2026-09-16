def write_points(self, points, time_precision=None, database=None,
    retention_policy=None, tags=None, batch_size=None, protocol='json',
    consistency=None):
    if batch_size and batch_size > 0:
        for batch in self._batches(points, batch_size):
            self._write_points(points=batch, time_precision=time_precision,
                database=database, retention_policy=retention_policy, tags=
                tags, protocol=protocol, consistency=consistency)
        return True
    return self._write_points(points=points, time_precision=time_precision,
        database=database, retention_policy=retention_policy, tags=tags,
        protocol=protocol, consistency=consistency)