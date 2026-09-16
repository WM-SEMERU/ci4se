def get_name_cost(db, name):
    lastblock = db.lastblock
    namespace_id = get_namespace_from_name(name)
    if namespace_id is None or len(namespace_id) == 0:
        log.debug("No namespace '%s'" % namespace_id)
        return None
    namespace = db.get_namespace(namespace_id)
    if namespace is None:
        log.debug("Namespace '{}' is being revealed".format(namespace_id))
        namespace = db.get_namespace_reveal(namespace_id)
    if namespace is None:
        log.debug("No namespace '%s'" % namespace_id)
        return None
    name_fee = price_name(get_name_from_fq_name(name), namespace, lastblock)
    name_fee_units = None
    if namespace['version'] == NAMESPACE_VERSION_PAY_WITH_STACKS:
        name_fee_units = TOKEN_TYPE_STACKS
    else:
        name_fee_units = 'BTC'
    name_fee = int(math.ceil(name_fee))
    log.debug("Cost of '%s' at %s is %s units of %s" % (name, lastblock,
        name_fee, name_fee_units))
    return {'amount': name_fee, 'units': name_fee_units}