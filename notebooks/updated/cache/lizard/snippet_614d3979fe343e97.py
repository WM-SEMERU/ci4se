def _get_qvm_based_on_real_device(name: str, device: Device, noisy: bool,
    connection: ForestConnection=None, qvm_type: str='qvm'):
    if noisy:
        noise_model = device.noise_model
    else:
        noise_model = None
    return _get_qvm_qc(name=name, connection=connection, device=device,
        noise_model=noise_model, requires_executable=True, qvm_type=qvm_type)