def apply_noise_model(prog, noise_model):
    new_prog = _noise_model_program_header(noise_model)
    for i in prog:
        if isinstance(i, Gate):
            try:
                _, new_name = get_noisy_gate(i.name, tuple(i.params))
                new_prog += Gate(new_name, [], i.qubits)
            except NoisyGateUndefined:
                new_prog += i
        else:
            new_prog += i
    return new_prog