def get_processor(self, entity_id, sp_config):
    processor_string = sp_config.get('processor', None)
    if processor_string:
        try:
            return import_string(processor_string)(entity_id)
        except Exception as e:
            logger.error('Failed to instantiate processor: {} - {}'.format(
                processor_string, e), exc_info=True)
            raise
    return BaseProcessor(entity_id)