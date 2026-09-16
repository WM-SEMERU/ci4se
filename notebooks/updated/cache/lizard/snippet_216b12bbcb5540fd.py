def unregister_counter_nonzero(network):
    if not hasattr(network, '__counter_nonzero_handles__'):
        raise ValueError(
            'register_counter_nonzero was not called for this network')
    for h in network.__counter_nonzero_handles__:
        h.remove()
    delattr(network, '__counter_nonzero_handles__')
    for module in network.modules():
        if hasattr(module, '__counter_nonzero__'):
            delattr(module, '__counter_nonzero__')