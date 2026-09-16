def call(ezo, name, method, data, target):
    c, err = Contract.get(name, ezo)
    if err:
        return None, err
    address, err = Contract.get_address(name, c.hash, ezo.db, target)
    if err:
        return None, err
    params = c.paramsForMethod(method, data)
    address = ezo.w3.toChecksumAddress(address)
    ezo.w3.eth.defaultAccount = ezo.w3.toChecksumAddress(get_account(ezo.
        config, target))
    if not c.contract_obj:
        try:
            c.contract_obj = ezo.w3.eth.contract(address=address, abi=c.abi)
        except Exception as e:
            return None, e
    contract_func = c.contract_obj.functions[method]
    try:
        if not params:
            result = contract_func().call()
        else:
            result = contract_func(*params).call()
    except Exception as e:
        return None, 'error executing call: {}'.format(e)
    return result, None