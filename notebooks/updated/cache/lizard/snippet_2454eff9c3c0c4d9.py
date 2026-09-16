def get_live_url(con_pool, method, host, url, headers, retries=1, redirect=
    True, body=None, service_name=None):
    timeout = con_pool.timeout.read_timeout
    start_time = time.time()
    response = con_pool.urlopen(method, url, body=body, headers=headers,
        redirect=redirect, retries=retries, timeout=timeout)
    request_time = time.time() - start_time
    rest_request.send(sender='restclients', url=url, request_time=
        request_time, hostname=socket.gethostname(), service_name=service_name)
    rest_request_passfail.send(sender='restclients', url=url, success=True,
        hostname=socket.gethostname(), service_name=service_name)
    return response