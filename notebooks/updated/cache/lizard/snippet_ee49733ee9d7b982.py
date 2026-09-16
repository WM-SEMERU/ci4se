def status_webapp(app, url='http://localhost:8080/manager', timeout=180):
    webapps = ls(url, timeout=timeout)
    for i in webapps:
        if i == app:
            return webapps[i]['mode']
    return 'missing'