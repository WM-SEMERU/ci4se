def forwards(apps, schema_editor):
    Event = apps.get_model('spectator_events', 'Event')
    Work = apps.get_model('spectator_events', 'Work')
    WorkRole = apps.get_model('spectator_events', 'WorkRole')
    WorkSelection = apps.get_model('spectator_events', 'WorkSelection')
    for event in Event.objects.filter(kind='museum'):
        work = Work.objects.create(kind='exhibition', title=event.title,
            title_sort=event.title_sort)
        work.slug = generate_slug(work.pk)
        work.save()
        WorkSelection.objects.create(event=event, work=work)
        for role in event.roles.all():
            WorkRole.objects.create(creator=role.creator, work=work,
                role_name=role.role_name, role_order=role.role_order)
            role.delete()