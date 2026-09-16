def set_port_info(self, webport, mediaport, httpsport, onvifport, callback=None
    ):
    params = {'webPort': webport, 'mediaPort': mediaport, 'httpsPort':
        httpsport, 'onvifPort': onvifport}
    return self.execute_command('setPortInfo', params, callback=callback)