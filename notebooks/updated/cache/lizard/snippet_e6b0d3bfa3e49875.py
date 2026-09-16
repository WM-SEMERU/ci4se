def verify_unsigned_tx(unsigned_tx, outputs, inputs=None, sweep_funds=False,
    change_address=None, coin_symbol='btc'):
    if not (change_address or sweep_funds):
        err_msg = (
            'Cannot Verify Without Developer Supplying Change Address (or Sweeping)'
            )
        return False, err_msg
    if 'tosign_tx' not in unsigned_tx:
        err_msg = 'tosign_tx not in API response:\n%s' % unsigned_tx
        return False, err_msg
    output_addr_list = [x['address'] for x in outputs if x.get('address') !=
        None]
    if change_address:
        output_addr_list.append(change_address)
    assert len(unsigned_tx['tosign_tx']) == len(unsigned_tx['tosign']
        ), unsigned_tx
    for cnt, tosign_tx_toverify in enumerate(unsigned_tx['tosign_tx']):
        if double_sha256(tosign_tx_toverify) != unsigned_tx['tosign'][cnt]:
            err_msg = 'double_sha256(%s) =! %s' % (tosign_tx_toverify,
                unsigned_tx['tosign'][cnt])
            print(unsigned_tx)
            return False, err_msg
        try:
            txn_outputs_response_dict = get_txn_outputs_dict(raw_tx_hex=
                tosign_tx_toverify, output_addr_list=output_addr_list,
                coin_symbol=coin_symbol)
        except Exception as inst:
            print(unsigned_tx)
            print(coin_symbol)
            return False, str(inst)
        if sweep_funds:
            continue
        else:
            try:
                txn_outputs_response_dict.pop(change_address)
            except KeyError:
                pass
        user_outputs = compress_txn_outputs(outputs)
        if txn_outputs_response_dict != user_outputs:
            err_msg = 'API Response Ouputs != Supplied Outputs\n\n%s\n\n%s' % (
                txn_outputs_response_dict, user_outputs)
            return False, err_msg
    return True, ''