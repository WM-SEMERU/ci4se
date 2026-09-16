def transfer_from(self, spender_acct: Account, b58_from_address: str,
    b58_to_address: str, value: int, payer_acct: Account, gas_limit: int,
    gas_price: int):
    func = InvokeFunction('transferFrom')
    Oep4.__b58_address_check(b58_from_address)
    Oep4.__b58_address_check(b58_to_address)
    if not isinstance(spender_acct, Account):
        raise SDKException(ErrorCode.param_err(
            'the data type of spender_acct should be Account.'))
    spender_address_array = spender_acct.get_address().to_bytes()
    from_address_array = Address.b58decode(b58_from_address).to_bytes()
    to_address_array = Address.b58decode(b58_to_address).to_bytes()
    if not isinstance(value, int):
        raise SDKException(ErrorCode.param_err(
            'the data type of value should be int.'))
    func.set_params_value(spender_address_array, from_address_array,
        to_address_array, value)
    params = func.create_invoke_code()
    unix_time_now = int(time.time())
    params.append(103)
    bytearray_contract_address = bytearray.fromhex(self.__hex_contract_address)
    bytearray_contract_address.reverse()
    for i in bytearray_contract_address:
        params.append(i)
    if payer_acct is None:
        raise SDKException(ErrorCode.param_err('payer account is None.'))
    payer_address_array = payer_acct.get_address().to_bytes()
    tx = Transaction(0, 209, unix_time_now, gas_price, gas_limit,
        payer_address_array, params, bytearray(), [])
    tx.sign_transaction(spender_acct)
    if spender_acct.get_address_base58() != payer_acct.get_address_base58():
        tx.add_sign_transaction(payer_acct)
    tx_hash = self.__sdk.get_network().send_raw_transaction(tx)
    return tx_hash