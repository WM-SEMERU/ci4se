def Run(self, unused_arg):
    logging.debug('Disabling service')
    win32serviceutil.ChangeServiceConfig(None, config.CONFIG[
        'Nanny.service_name'], startType=win32service.SERVICE_DISABLED)
    svc_config = QueryService(config.CONFIG['Nanny.service_name'])
    if svc_config[1] == win32service.SERVICE_DISABLED:
        logging.info('Disabled service successfully')
        self.SendReply(rdf_protodict.DataBlob(string='Service disabled.'))
    else:
        self.SendReply(rdf_protodict.DataBlob(string=
            'Service failed to disable.'))