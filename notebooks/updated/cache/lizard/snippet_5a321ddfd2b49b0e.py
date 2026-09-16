def _is_valid_netmask(self, prefixlen):
    try:
        prefixlen = int(prefixlen)
    except ValueError:
        return False
    return 0 <= prefixlen <= self._max_prefixlen