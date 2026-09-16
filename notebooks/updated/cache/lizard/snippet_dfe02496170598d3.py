def create_wallet_from_address(wallet_name, address, api_key, coin_symbol='btc'
    ):
    assert is_valid_address_for_coinsymbol(address, coin_symbol)
    assert api_key
    assert is_valid_wallet_name(wallet_name), wallet_name
    data = {'name': wallet_name, 'addresses': [address]}
    params = {'token': api_key}
    url = make_url(coin_symbol, 'wallets')
    r = requests.post(url, json=data, params=params, verify=True, timeout=
        TIMEOUT_IN_SECONDS)
    return get_valid_json(r)