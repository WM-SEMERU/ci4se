def records(rec_type=None, fields=None, clean=True):
    if rec_type is None:
        smbios = _dmi_parse(_dmidecoder(), clean, fields)
    else:
        smbios = _dmi_parse(_dmidecoder('-t {0}'.format(rec_type)), clean,
            fields)
    return smbios