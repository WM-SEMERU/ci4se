def placeholder_plugin_filter(self, request, queryset):
    if not request:
        return queryset
    if GLL.is_active:
        return queryset.filter(language=GLL.language_code)
    return queryset