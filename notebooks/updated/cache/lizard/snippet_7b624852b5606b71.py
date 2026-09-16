def wait_for_winrm(host, port, username, password, timeout=900, use_ssl=
    True, verify=True):
    wait_for_port(host=host, port=port, timeout=timeout)
    start = time.time()
    log.debug('Attempting WinRM connection to host %s on port %s', host, port)
    transport = 'ssl'
    if not use_ssl:
        transport = 'ntlm'
    trycount = 0
    while True:
        trycount += 1
        try:
            winrm_kwargs = {'target': host, 'auth': (username, password),
                'transport': transport}
            if not verify:
                log.debug('SSL validation for WinRM disabled.')
                winrm_kwargs['server_cert_validation'] = 'ignore'
            s = winrm.Session(**winrm_kwargs)
            if hasattr(s.protocol, 'set_timeout'):
                s.protocol.set_timeout(15)
            log.trace('WinRM endpoint url: %s', s.url)
            r = s.run_cmd('sc query winrm')
            if r.status_code == 0:
                log.debug('WinRM session connected...')
                return s
            log.debug('Return code was %s', r.status_code)
        except WinRMTransportError as exc:
            log.debug('Caught exception in wait_for_winrm: %s', exc)
        except InvalidCredentialsError as exc:
            log.error(
                "Caught Invalid Credentials error in wait_for_winrm.  You may have an incorrect username/password, the new minion's WinRM configuration is not correct, the customization spec has not finished, or we are waiting for an account rename policy to take effect.  Connection attempts will continue to be made until the WinRM timeout has been exceeded."
                )
        except ReadTimeout as exc:
            log.error('Caught Read Timeout while waiting for winrm.')
        except ConnectionError as exc:
            log.error(
                'Caught Connection Error while waiting for winrm.  Connection attempts will continue to be made until the WinRM timeout has been exceeded.'
                )
        if time.time() - start > timeout:
            log.error('WinRM connection timed out: %s', timeout)
            return None
        log.debug('Retrying WinRM connection to host %s on port %s (try %s)',
            host, port, trycount)
        time.sleep(1)