def _web_scan(self, web):
    try:
        req = requests.head(web['url'], allow_redirects=True, verify=web[
            'ssl_verify'], proxies=web['proxies'], timeout=web['timeout'])
    except Exception as e:
        logger.debug(e)
        web['status'] = 'Error'
        web['elapsed'] = 0
    else:
        web['status'] = req.status_code
        web['elapsed'] = req.elapsed.total_seconds()
    return web