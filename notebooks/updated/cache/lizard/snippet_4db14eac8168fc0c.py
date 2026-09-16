def process_mock_rpc(input_string):
    spec, equals, value = input_string.partition('=')
    if len(equals) == 0:
        print('Could not parse mock RPC argument: {}'.format(input_string))
        sys.exit(1)
    try:
        value = int(value.strip(), 0)
    except ValueError as exc:
        print('Could not parse mock RPC value: {}'.format(str(exc)))
        sys.exit(1)
    slot, part, rpc_id = spec.partition(':')
    if len(part) == 0:
        print('Could not parse mock RPC slot/rpc definition: {}'.format(spec))
        sys.exit(1)
    try:
        slot = SlotIdentifier.FromString(slot)
    except ArgumentError as exc:
        print('Could not parse slot id in mock RPC definition: {}'.format(
            exc.msg))
        sys.exit(1)
    try:
        rpc_id = int(rpc_id, 0)
    except ValueError as exc:
        print('Could not parse mock RPC number: {}'.format(str(exc)))
        sys.exit(1)
    return slot, rpc_id, value