def _app_config_select(self, request, obj):
    if not obj and not request.GET.get(self.app_config_attribute, False):
        config_model = get_apphook_model(self.model, self.app_config_attribute)
        if config_model.objects.count() == 1:
            return config_model.objects.first()
        return None
    elif obj and getattr(obj, self.app_config_attribute, False):
        return getattr(obj, self.app_config_attribute)
    elif request.GET.get(self.app_config_attribute, False):
        config_model = get_apphook_model(self.model, self.app_config_attribute)
        return config_model.objects.get(pk=int(request.GET.get(self.
            app_config_attribute, False)))
    return False