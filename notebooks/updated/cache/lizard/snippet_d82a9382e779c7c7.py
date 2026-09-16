def start(name, runas=None):
    return prlctl('start', salt.utils.data.decode(name), runas=runas)