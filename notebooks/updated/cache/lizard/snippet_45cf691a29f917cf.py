def survey(network=None, path='', pattern='', log=False):
    if log:
        logger.setLevel(logging.DEBUG)
    else:
        logger.setLevel(logging.CRITICAL)
    network_scan = asyncio.ensure_future(asynchronous(urls=url_generator(
        network=network, path=path), re_filter=re.compile(pattern)))
    ioloop = asyncio.get_event_loop()
    ioloop.run_until_complete(network_scan)
    ioloop.run_until_complete(asyncio.sleep(0))
    return sorted(network_scan.result(), key=lambda x: ipaddress.ip_address
        (x.hostname))