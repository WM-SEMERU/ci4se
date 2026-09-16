def clean_deleted_sessions(cls):
    for federate_slo in cls.objects.all():
        if not SessionStore(session_key=federate_slo.session_key).get(
            'authenticated'):
            federate_slo.delete()