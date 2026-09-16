def get_temp_dir(keep=False):
    dname = tempfile.mkdtemp(prefix='scapy')
    if not keep:
        conf.temp_files.append(dname)
    return dname