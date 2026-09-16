def _write_file(iface, data, folder, pattern):
    filename = os.path.join(folder, pattern.format(iface))
    if not os.path.exists(folder):
        msg = '{0} cannot be written. {1} does not exist'
        msg = msg.format(filename, folder)
        log.error(msg)
        raise AttributeError(msg)
    with salt.utils.files.flopen(filename, 'w') as fout:
        fout.write(salt.utils.stringutils.to_str(data))
    return filename