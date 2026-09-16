def create_temporary_ca_file(anchor_list):
    try:
        f, fname = tempfile.mkstemp()
        for a in anchor_list:
            s = a.output(fmt='PEM')
            l = os.write(f, s)
        os.close(f)
    except:
        return None
    return fname