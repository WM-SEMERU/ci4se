def get_context_data(self, **kwargs):
    context = super(UserServiceUpdateView, self).get_context_data(**kwargs)
    context['service_name_alone'] = self.object.name.name.rsplit('Service')[1]
    context['service_name'] = self.object.name.name
    context['SERVICES_AUTH'] = settings.SERVICES_AUTH
    context['SERVICES_HOSTED_WITH_AUTH'] = settings.SERVICES_HOSTED_WITH_AUTH
    context['SERVICES_NEUTRAL'] = settings.SERVICES_NEUTRAL
    context['action'] = 'edit'
    return context