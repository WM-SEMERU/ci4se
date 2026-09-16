def save_model(self, request, obj, form, change):
    like_metrics = self.model.objects.filter(name=obj.name)
    updates = {}
    for key in form.changed_data:
        updates[key] = form.cleaned_data[key]
    like_metrics.update(**updates)