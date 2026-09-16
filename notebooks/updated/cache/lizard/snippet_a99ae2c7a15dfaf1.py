def get_list_filter(self, request):
    original = super(TrackedLiveAdmin, self).get_list_filter(request)
    return original + type(original)([PeriodFilter])