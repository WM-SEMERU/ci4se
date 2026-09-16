def set_data_location(apps, schema_editor):
    Data = apps.get_model('flow', 'Data')
    DataLocation = apps.get_model('flow', 'DataLocation')
    for data in Data.objects.all():
        if os.path.isdir(os.path.join(settings.FLOW_EXECUTOR['DATA_DIR'],
            str(data.id))):
            with transaction.atomic():
                data_location = DataLocation.objects.create(id=data.id,
                    subpath=str(data.id))
                data_location.data.add(data)
    if DataLocation.objects.exists():
        max_id = DataLocation.objects.order_by('id').last().id
        with connection.cursor() as cursor:
            cursor.execute(
                'ALTER SEQUENCE flow_datalocation_id_seq RESTART WITH {};'.
                format(max_id + 1))