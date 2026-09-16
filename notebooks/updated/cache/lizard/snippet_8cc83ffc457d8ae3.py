def queryset(self, request, queryset):
    if self.value() == '-1':
        return queryset.filter(latest_version__isnull=True)
    elif self.value() == '0':
        return queryset.filter(current_version__isnull=False,
            latest_version__isnull=False, latest_version=F('current_version'))
    elif self.value() == '1':
        return queryset.filter(current_version__isnull=False,
            latest_version__isnull=False).exclude(latest_version=F(
            'current_version'))
    else:
        return queryset