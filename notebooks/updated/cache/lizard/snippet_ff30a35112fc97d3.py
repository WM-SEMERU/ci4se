def ini_dump_hook(cfg, text: bool=False):
    data = cfg.config.dump()
    ndict = {}
    for key, item in data.items():
        key = key.replace('_', '.')
        ndict[key] = item
    cfg.tmpini = configparser.ConfigParser()
    cfg.tmpini.read_dict(data)
    if not text:
        cfg.tmpini.write(cfg.fd)
    else:
        return
    cfg.reload()