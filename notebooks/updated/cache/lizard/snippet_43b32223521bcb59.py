def get_queryset(self):
    kwargs = {}
    if self.start_at:
        kwargs.update({('%s__gte' % self.date_field): self.start_at})
    return super(DateRangeMixin, self).get_queryset().filter(**kwargs)