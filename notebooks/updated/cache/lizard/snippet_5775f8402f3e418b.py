def _populate_attributes(self, config, record, context, data):
    search_return_attributes = config['search_return_attributes']
    for attr in search_return_attributes.keys():
        if attr in record['attributes']:
            if record['attributes'][attr]:
                data.attributes[search_return_attributes[attr]] = record[
                    'attributes'][attr]
                satosa_logging(logger, logging.DEBUG,
                    'Setting internal attribute {} with values {}'.format(
                    search_return_attributes[attr], record['attributes'][
                    attr]), context.state)
            else:
                satosa_logging(logger, logging.DEBUG,
                    'Not setting internal attribute {} because value {} is null or empty'
                    .format(search_return_attributes[attr], record[
                    'attributes'][attr]), context.state)