def parse_tx_op_return(tx):
    op_return = None
    outputs = tx['vout']
    for out in outputs:
        script_key = out['scriptPubKey']['hex']
        if int(script_key[0:2], 16) == virtualchain.OPCODE_VALUES['OP_RETURN']:
            op_return = script_key.decode('hex')
            break
    if op_return is None:
        msg = 'transaction has no OP_RETURN output'
        log.error(msg)
        log.debug('{}:\n{}'.format(msg, simplejson.dumps(tx)))
        return None, None
    magic = op_return[2:4]
    if magic != blockstack_magic_bytes():
        msg = 'OP_RETURN output does not encode a blockchain ID operation'
        log.error(msg)
        return None, None
    opcode, payload = op_return[4], op_return[5:]
    return opcode, payload