def _get_co_name(self, context):
    try:
        co_name = context.state[self.name][self.KEY_CO_NAME]
        logger.debug('Found CO {} from state'.format(co_name))
    except KeyError:
        co_name = self._get_co_name_from_path(context)
        logger.debug('Found CO {} from request path'.format(co_name))
    return co_name