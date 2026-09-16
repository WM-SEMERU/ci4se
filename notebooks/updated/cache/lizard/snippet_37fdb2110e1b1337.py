def queryset(self, request, queryset):
    if self.value() is not None:
        return queryset.filter(information__type__pk=self.value())
    else:
        return queryset