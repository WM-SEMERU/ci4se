def get(self, request, *args, **kwargs):
    queryset = self.get_selected(request)
    return self.render(request, queryset=queryset)