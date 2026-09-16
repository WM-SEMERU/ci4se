def get_compiler(self, *args, **kwargs):
    if self.querytime.active and (not hasattr(self,
        '_querytime_filter_added') or not self._querytime_filter_added):
        time = self.querytime.time
        if time is None:
            self.add_q(Q(version_end_date__isnull=True))
        else:
            self.add_q((Q(version_end_date__gt=time) | Q(
                version_end_date__isnull=True)) & Q(version_start_date__lte
                =time))
        self._querytime_filter_added = True
    return super(VersionedQuery, self).get_compiler(*args, **kwargs)