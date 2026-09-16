def _splash():
    splash_title = '{pkg} [{version}] - {url}'.format(pkg=PKG_NAME, version
        =version, url=PKG_URL)
    log.to_stdout(splash_title, colorf=log.yellow, bold=True)
    log.to_stdout('-' * len(splash_title), colorf=log.yellow, bold=True)