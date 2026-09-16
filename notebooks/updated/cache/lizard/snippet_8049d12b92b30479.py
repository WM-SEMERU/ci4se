def do_function(self, prov, func, kwargs):
    matches = self.lookup_providers(prov)
    if len(matches) > 1:
        raise SaltCloudSystemExit(
            "More than one results matched '{0}'. Please specify one of: {1}"
            .format(prov, ', '.join(['{0}:{1}'.format(alias, driver) for 
            alias, driver in matches])))
    alias, driver = matches.pop()
    fun = '{0}.{1}'.format(driver, func)
    if fun not in self.clouds:
        raise SaltCloudSystemExit(
            "The '{0}' cloud provider alias, for the '{1}' driver, does not define the function '{2}'"
            .format(alias, driver, func))
    log.debug("Trying to execute '%s' with the following kwargs: %s", fun,
        kwargs)
    with salt.utils.context.func_globals_inject(self.clouds[fun],
        __active_provider_name__=':'.join([alias, driver])):
        if kwargs:
            return {alias: {driver: self.clouds[fun](call='function',
                kwargs=kwargs)}}
        return {alias: {driver: self.clouds[fun](call='function')}}