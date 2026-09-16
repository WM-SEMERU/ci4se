def exclude_current_instance(self, queryset):
    if self.instance is not None:
        return queryset.exclude(pk=self.instance.pk)
    return queryset