def add_timeframed_query_manager(sender, **kwargs):
    if not issubclass(sender, TimeFramedModel):
        return
    if _field_exists(sender, 'timeframed'):
        raise ImproperlyConfigured(
            "Model '%s' has a field named 'timeframed' which conflicts with the TimeFramedModel manager."
             % sender.__name__)
    sender.add_to_class('timeframed', QueryManager((models.Q(start__lte=now
        ) | models.Q(start__isnull=True)) & (models.Q(end__gte=now) |
        models.Q(end__isnull=True))))