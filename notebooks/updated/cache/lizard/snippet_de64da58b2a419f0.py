def delete_forwarding_address(payment_id, coin_symbol='btc', api_key=None):
    assert payment_id, 'payment_id required'
    assert is_valid_coin_symbol(coin_symbol)
    assert api_key, 'api_key required'
    params = {'token': api_key}
    url = make_url(**dict(payments=payment_id))
    r = requests.delete(url, params=params, verify=True, timeout=
        TIMEOUT_IN_SECONDS)
    return get_valid_json(r, allow_204=True)