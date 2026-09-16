def _explicit_close(napalm_device):
    if salt.utils.napalm.not_always_alive(__opts__):
        try:
            napalm_device['DRIVER'].close()
        except Exception as err:
            log.error('Unable to close the temp connection with the device:')
            log.error(err)
            log.error('Please report.')