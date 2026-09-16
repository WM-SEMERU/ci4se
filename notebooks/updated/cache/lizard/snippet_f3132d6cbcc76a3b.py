def validate_address(value):
    if is_bytes(value):
        if not is_binary_address(value):
            raise InvalidAddress(
                'Address must be 20 bytes when input type is bytes', value)
        return
    if not isinstance(value, str):
        raise TypeError('Address {} must be provided as a string'.format(value)
            )
    if not is_hex_address(value):
        raise InvalidAddress(
            'Address must be 20 bytes, as a hex string with a 0x prefix', value
            )
    if not is_checksum_address(value):
        if value == value.lower():
            raise InvalidAddress(
                'Web3.py only accepts checksum addresses. The software that gave you this non-checksum address should be considered unsafe, please file it as a bug on their platform. Try using an ENS name instead. Or, if you must accept lower safety, use Web3.toChecksumAddress(lower_case_address).'
                , value)
        else:
            raise InvalidAddress(
                'Address has an invalid EIP-55 checksum. After looking up the address from the original source, try again.'
                , value)