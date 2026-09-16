def check_payment_v3(state_engine, state_op_type, nameop, fee_block_id,
    token_address, burn_address, name_fee, block_id):
    epoch_features = get_epoch_features(block_id)
    name = nameop['name']
    namespace_id = get_namespace_from_name(name)
    name_without_namespace = get_name_from_fq_name(name)
    namespace = state_engine.get_namespace(namespace_id)
    assert namespace['version'] == NAMESPACE_VERSION_PAY_WITH_STACKS
    if EPOCH_FEATURE_NAMESPACE_PAY_WITH_STACKS not in epoch_features:
        log.warning(
            "Name '{}' was created in namespace '{}', with version bits 0x{:x}, which is not supported in this epoch"
            .format(name, namespace['namespace_id'], namespace['version']))
        return {'status': False}
    if burn_address != BLOCKSTACK_BURN_ADDRESS:
        log.warning('Buyer of {} used the wrong burn address ({}): expected {}'
            .format(name, burn_address, BLOCKSTACK_BURN_ADDRESS))
        return {'status': False}
    stacks_payment_info = get_stacks_payment(state_engine, nameop,
        state_op_type)
    if not stacks_payment_info['status']:
        return {'status': False}
    stacks_price = price_name(name_without_namespace, namespace, fee_block_id)
    res = check_token_payment(name, stacks_price, stacks_payment_info)
    if not res['status']:
        return {'status': False}
    tokens_paid = stacks_payment_info['tokens_paid']
    token_units = stacks_payment_info['token_units']
    return {'status': True, 'tokens_paid': tokens_paid, 'token_units':
        token_units}