def per_from_id(flavors=chat_flavors + inline_flavors):
    return _wrap_none(lambda msg: msg['from']['id'] if flavors == 'all' or 
        flavor(msg) in flavors else None)