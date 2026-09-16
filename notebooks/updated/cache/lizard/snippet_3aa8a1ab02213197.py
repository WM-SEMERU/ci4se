def unify_partitions(self):
    partitions = self.collect_segment_partitions()
    with self.progress.start('coalesce', 0, message=
        'Coalescing partition segments') as ps:
        for name, segments in iteritems(partitions):
            ps.add(item_type='partitions', item_count=len(segments),
                message='Colescing partition {}'.format(name))
            self.unify_partition(name, segments, ps)