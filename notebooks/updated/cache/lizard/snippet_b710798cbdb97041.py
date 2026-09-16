def sources_list(ruby=None, runas=None, gem_bin=None):
    ret = _gem(['sources'], ruby, gem_bin=gem_bin, runas=runas)
    return [] if ret is False else ret.splitlines()[2:]