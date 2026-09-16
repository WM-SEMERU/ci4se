def by_publications(self):
    if not spectator_apps.is_enabled('reading'):
        raise ImproperlyConfigured(
            "To use the CreatorManager.by_publications() method, 'spectator.reading' must by in INSTALLED_APPS."
            )
    qs = self.get_queryset()
    qs = qs.exclude(publications__reading__isnull=True).annotate(
        num_publications=Count('publications')).order_by('-num_publications',
        'name_sort')
    return qs