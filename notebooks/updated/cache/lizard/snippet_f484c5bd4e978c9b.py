def compute_service_descriptor(price, consume_endpoint, service_endpoint,
    timeout):
    return ServiceTypes.CLOUD_COMPUTE, {'price': price, 'consumeEndpoint':
        consume_endpoint, 'serviceEndpoint': service_endpoint, 'timeout':
        timeout}