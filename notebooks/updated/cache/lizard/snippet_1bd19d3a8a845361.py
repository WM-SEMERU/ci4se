def services(namespace='default', **kwargs):
    cfg = _setup_conn(**kwargs)
    try:
        api_instance = kubernetes.client.CoreV1Api()
        api_response = api_instance.list_namespaced_service(namespace)
        return [srv['metadata']['name'] for srv in api_response.to_dict().
            get('items')]
    except (ApiException, HTTPError) as exc:
        if isinstance(exc, ApiException) and exc.status == 404:
            return None
        else:
            log.exception(
                'Exception when calling CoreV1Api->list_namespaced_service')
            raise CommandExecutionError(exc)
    finally:
        _cleanup(**cfg)