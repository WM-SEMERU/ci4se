def get_formset(self):
    if self.widget:
        queryset = self.widget.dimensions
    else:
        queryset = WidgetDimension.objects.none()
    if self._formset is None:
        self._formset = self.formset_class(self.request.POST or None,
            initial=self._get_formset_data(), prefix=self._meta.name,
            queryset=queryset)
    return self._formset