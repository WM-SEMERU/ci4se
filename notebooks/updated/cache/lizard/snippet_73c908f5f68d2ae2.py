def wait_for_service(host, port, timeout=DEFAULT_TIMEOUT):
    service = ServiceURL('tcp://{}:{}'.format(host, port), timeout)
    return service.wait()