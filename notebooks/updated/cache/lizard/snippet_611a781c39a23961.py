def stream_entry_assemble(hasher, file, eccfile, entry_fields,
    max_block_size, header_size, resilience_rates, constantmode=False):
    eccfile.seek(entry_fields['ecc_field_pos'][0])
    curpos = file.tell()
    ecc_curpos = eccfile.tell()
    while ecc_curpos < entry_fields['ecc_field_pos'][1]:
        if curpos < header_size or constantmode:
            rate = resilience_rates[0]
        else:
            rate = feature_scaling(curpos, header_size, entry_fields[
                'filesize'], resilience_rates[1], resilience_rates[2])
        ecc_params = compute_ecc_params(max_block_size, rate, hasher)
        mes = file.read(ecc_params['message_size'])
        if len(mes) == 0:
            return
        buf = eccfile.read(ecc_params['hash_size'] + ecc_params['ecc_size'])
        hash = buf[:ecc_params['hash_size']]
        ecc = buf[ecc_params['hash_size']:]
        yield {'message': mes, 'hash': hash, 'ecc': ecc, 'rate': rate,
            'ecc_params': ecc_params, 'curpos': curpos, 'ecc_curpos':
            ecc_curpos}
        curpos = file.tell()
        ecc_curpos = eccfile.tell()
    file.seek(0, os.SEEK_END)
    size = file.tell()
    if curpos < size:
        print(
            'WARNING: end of ecc track reached but not the end of file! Either the ecc ending marker was misdetected, or either the file hash changed! Some blocks maybe may not have been properly checked!'
            )