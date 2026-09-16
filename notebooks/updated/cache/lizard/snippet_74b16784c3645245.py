def _proxy_kwargs(browser_name, proxy, browser_kwargs={}):
    proxy_dict = {'httpProxy': proxy.proxy, 'proxyType': 'manual'}
    if (browser_name == 'firefox' and 'desired_capabilities' not in
        browser_kwargs):
        wd_proxy = webdriver.common.proxy.Proxy(proxy_dict)
        browser_kwargs['proxy'] = wd_proxy
    else:
        if 'desired_capabilities' not in browser_kwargs:
            browser_kwargs['desired_capabilities'] = {}
        browser_kwargs['desired_capabilities']['proxy'] = proxy_dict
    return browser_kwargs