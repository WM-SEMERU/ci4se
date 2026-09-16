def oaiid_fetcher(record_uuid, data):
    pid_value = data.get('_oai', {}).get('id')
    if pid_value is None:
        raise PersistentIdentifierError()
    return FetchedPID(provider=OAIIDProvider, pid_type=OAIIDProvider.
        pid_type, pid_value=str(pid_value))