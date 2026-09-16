def p2wsh_input_and_witness(outpoint, stack, witness_script, sequence=None):
    if sequence is None:
        sequence = guess_sequence(witness_script)
    stack = list(map(lambda x: b'' if x == 'NONE' else bytes.fromhex(x),
        stack.split()))
    stack.append(script_ser.serialize(witness_script))
    return tb.make_witness_input_and_witness(outpoint, sequence, stack)