def _check_suffix(self, w_string, access_string, index):
    prefix_as = self._membership_query(access_string)
    full_as = self._membership_query(access_string + w_string[index:])
    prefix_w = self._membership_query(w_string[:index])
    full_w = self._membership_query(w_string)
    length = len(commonprefix([prefix_as, full_as]))
    as_suffix = full_as[length:]
    length = len(commonprefix([prefix_w, full_w]))
    w_suffix = full_w[length:]
    if as_suffix != w_suffix:
        logging.debug('Access string state incorrect')
        return True
    logging.debug('Access string state correct.')
    return False