def update_nonce(input_params):
    input_cp = input_params.copy()
    if len(input_cp.get('nonce', '')) == 0:
        input_cp['nonce'] = str(Nonce())
    return input_cp