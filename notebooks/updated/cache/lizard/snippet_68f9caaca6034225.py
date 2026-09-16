def check_payment(state_engine, state_op_type, nameop, fee_block_id,
    token_address, burn_address, name_fee, block_id):
    assert state_op_type in ['NAME_REGISTRATION', 'NAME_RENEWAL'
        ], 'Invalid op type {}'.format(state_op_type)
    assert name_fee is not None
    assert isinstance(name_fee, (int, long))
    name = nameop['name']
    namespace_id = get_namespace_from_name(name)
    namespace = state_engine.get_namespace(namespace_id)
    res = None
    log.debug('{} is a version-0x{} namespace'.format(namespace[
        'namespace_id'], namespace['version']))
    if namespace['version'] == NAMESPACE_VERSION_PAY_TO_BURN:
        res = check_payment_v1(state_engine, state_op_type, nameop,
            fee_block_id, token_address, burn_address, name_fee, block_id)
    elif namespace['version'] == NAMESPACE_VERSION_PAY_TO_CREATOR:
        res = check_payment_v2(state_engine, state_op_type, nameop,
            fee_block_id, token_address, burn_address, name_fee, block_id)
    elif namespace['version'] == NAMESPACE_VERSION_PAY_WITH_STACKS:
        res = check_payment_v3(state_engine, state_op_type, nameop,
            fee_block_id, token_address, burn_address, name_fee, block_id)
    else:
        log.warning(
            'Namespace {} has version bits 0x{:x}, which has unknown registration rules'
            .format(namespace['namespace_id'], namespace['version']))
        return {'status': False}
    if not res['status']:
        return res
    tokens_paid = res['tokens_paid']
    token_units = res['token_units']
    return {'status': True, 'tokens_paid': tokens_paid, 'token_units':
        token_units}