def recalculate_estimate(recalculate_total=False):
    CostTrackingRegister.autodiscover()
    for resource_model in CostTrackingRegister.registered_resources:
        for resource in resource_model.objects.all():
            _update_resource_consumed(resource, recalculate_total=
                recalculate_total)
    ancestors_models = [m for m in models.PriceEstimate.
        get_estimated_models() if not issubclass(m, structure_models.
        ResourceMixin)]
    for model in ancestors_models:
        for ancestor in model.objects.all():
            _update_ancestor_consumed(ancestor)