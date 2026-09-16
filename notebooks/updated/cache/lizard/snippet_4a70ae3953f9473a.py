def _reload_if_necessary(self, env):
    try:
        mod = sys.modules[self.provider_module_name]
    except KeyError:
        mod = None
    if mod is None or mod.provmod_timestamp != os.path.getmtime(self.provid):
        logger = env.get_logger()
        logger.log_debug('Need to reload provider at %s' % self.provid)
        if self.provmod and hasattr(self.provmod, 'shutdown'):
            self.provmod.shutdown(env)
        try:
            del sys.modules[self.provider_module_name]
        except KeyError:
            pass
        try:
            self._load_provider_source(logger)
            self._init_provider(env)
        except IOError as exc:
            raise pywbem.CIMError(pywbem.CIM_ERR_FAILED, 
                'Error loading provider %s: %s' % (provid, exc))