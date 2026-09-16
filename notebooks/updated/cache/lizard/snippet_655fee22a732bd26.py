def get_temp_file(keep=False, autoext='', fd=False):
    f = tempfile.NamedTemporaryFile(prefix='scapy', suffix=autoext, delete=
        False)
    if not keep:
        conf.temp_files.append(f.name)
    if fd:
        return f
    else:
        f.close()
        return f.name