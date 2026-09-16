def _create_co_virtual_idp(self, context):
    co_name = self._get_co_name(context)
    context.decorate(self.KEY_CO_NAME, co_name)
    co_names = self._co_names_from_config()
    if co_name not in co_names:
        msg = 'CO {} not in configured list of COs {}'.format(co_name, co_names
            )
        satosa_logging(logger, logging.WARN, msg, context.state)
        raise SATOSAError(msg)
    backend_name = context.target_backend
    idp_config = copy.deepcopy(self.idp_config)
    idp_config = self._add_endpoints_to_config(idp_config, co_name,
        backend_name)
    idp_config = self._add_entity_id(idp_config, co_name)
    pysaml2_idp_config = IdPConfig().load(idp_config, metadata_construction
        =False)
    server = Server(config=pysaml2_idp_config)
    return server