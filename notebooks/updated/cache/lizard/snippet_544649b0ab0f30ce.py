def create_teams(obj, user, access):
    for field_name, access_types in access.items():
        id_field = '{}_id'.format(field_name)
        if hasattr(obj, id_field) and getattr(obj, id_field) is None:
            next_pk = next(iter(instance.pk for instance in obj.__class__.
                objects.order_by('-pk')), 0) + 1
            team_name = '{} for {} {}'.format(field_name, obj._meta.
                model_name, next_pk)
            new_team = Team(name=team_name, member_access=access_types[0],
                manager_access=access_types[1], creator=user)
            new_team.save()
            setattr(obj, field_name, new_team)
    return obj