def get_epoch_namespace_lifetime_multiplier(block_height, namespace_id):
    epoch_config = get_epoch_config(block_height)
    if epoch_config['namespaces'].has_key(namespace_id):
        return epoch_config['namespaces'][namespace_id][
            'NAMESPACE_LIFETIME_MULTIPLIER']
    else:
        return epoch_config['namespaces']['*']['NAMESPACE_LIFETIME_MULTIPLIER']