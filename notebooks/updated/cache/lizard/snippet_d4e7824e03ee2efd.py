def download_blood_vessels():
    local_path, _ = _download_file('pvtu_blood_vessels/blood_vessels.zip')
    filename = os.path.join(local_path, 'T0000000500.pvtu')
    mesh = vtki.read(filename)
    mesh.set_active_vectors('velocity')
    return mesh