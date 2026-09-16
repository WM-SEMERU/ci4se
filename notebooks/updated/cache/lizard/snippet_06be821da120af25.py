def compound_id(obj):
    if isinstance(obj, (Category, Session)):
        raise TypeError('Compound IDs are not supported for this entry type')
    elif isinstance(obj, Event):
        return unicode(obj.id)
    elif isinstance(obj, Contribution):
        return '{}.{}'.format(obj.event_id, obj.id)
    elif isinstance(obj, SubContribution):
        return '{}.{}.{}'.format(obj.contribution.event_id, obj.
            contribution_id, obj.id)