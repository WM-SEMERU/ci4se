def repository_delete(name, hosts=None, profile=None):
    es = _get_instance(hosts, profile)
    try:
        result = es.snapshot.delete_repository(repository=name)
        return result.get('acknowledged', False)
    except elasticsearch.NotFoundError:
        return True
    except elasticsearch.TransportError as e:
        raise CommandExecutionError(
            'Cannot delete repository {0}, server returned code {1} with message {2}'
            .format(name, e.status_code, e.error))