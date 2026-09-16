def register_unused_addresses(wallet_obj, subchain_index, num_addrs=1):
    verbose_print(
        'register_unused_addresses called on subchain %s for %s addrs' % (
        subchain_index, num_addrs))
    assert type(subchain_index) is int, subchain_index
    assert type(num_addrs) is int, num_addrs
    assert num_addrs > 0
    mpub = wallet_obj.serialize_b58(private=False)
    coin_symbol = coin_symbol_from_mkey(mpub)
    wallet_name = get_blockcypher_walletname_from_mpub(mpub=mpub,
        subchain_indices=[0, 1])
    network = guess_network_from_mkey(mpub)
    derivation_response = derive_hd_address(api_key=BLOCKCYPHER_API_KEY,
        wallet_name=wallet_name, num_addresses=num_addrs, subchain_index=
        subchain_index, coin_symbol=coin_symbol)
    verbose_print('derivation_response:')
    verbose_print(derivation_response)
    address_paths = derivation_response['chains'][0]['chain_addresses']
    full_address_paths = verify_and_fill_address_paths_from_bip32key(
        address_paths=address_paths, master_key=mpub, network=network)
    return full_address_paths