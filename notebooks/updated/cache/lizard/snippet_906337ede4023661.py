def solidity_get_contract_key(all_contracts, filepath, contract_name):
    if contract_name in all_contracts:
        return contract_name
    else:
        if filepath is None:
            filename = '<stdin>'
        else:
            _, filename = os.path.split(filepath)
        contract_key = filename + ':' + contract_name
        return contract_key if contract_key in all_contracts else None