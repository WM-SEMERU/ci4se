def create_prod_build(self, *args, **kwargs):
    logger.warning(
        'prod (all-in-one) builds are deprecated, please use create_orchestrator_build (support will be removed in version 0.54)'
        )
    return self._do_create_prod_build(*args, **kwargs)