def set_slug(apps, schema_editor):
    Event = apps.get_model('spectator_events', 'Event')
    for e in Event.objects.all():
        e.slug = generate_slug(e.pk)
        e.save(update_fields=['slug'])