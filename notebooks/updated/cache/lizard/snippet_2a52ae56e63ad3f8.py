def get_pseudo_abi_for_input(s, timeout=None, proxies=None):
    sighash = Utils.bytes_to_str(s[:4])
    for pseudo_abi in FourByteDirectory.get_pseudo_abi_for_sighash(sighash,
        timeout=timeout, proxies=proxies):
        types = [ti['type'] for ti in pseudo_abi['inputs']]
        try:
            _ = decode_abi(types, s[4:])
            yield pseudo_abi
        except eth_abi.exceptions.DecodingError as e:
            continue