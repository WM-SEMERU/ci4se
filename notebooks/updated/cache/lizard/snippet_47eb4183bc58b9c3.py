def get_signatures_from_script(script):
    script = script[1:]
    sigs = []
    while len(script) > 0:
        val, script = read_var_int(script)
        potential_sig, script = read_bytes(script, val)
        try:
            der_to_cdata(potential_sig[:-1])
            sigs.append(potential_sig)
        except ValueError:
            pass
    return sigs