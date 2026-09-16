def get_handlers(self, component_context, instance):
    logger_field = component_context.get_handler(constants.HANDLER_LOGGER)
    if not logger_field:
        _logger.warning("Logger iPOPO handler can't find its configuration")
        return []
    else:
        return [_LoggerHandler(logger_field, component_context.name)]