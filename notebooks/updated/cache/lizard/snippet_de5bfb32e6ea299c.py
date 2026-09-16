def rs_correct_msg_nofsynd(msg_in, nsym, fcr=0, generator=2, erase_pos=None,
    only_erasures=False):
    global field_charac
    if len(msg_in) > field_charac:
        raise ValueError('Message is too long (%i when max is %i)' % (len(
            msg_in), field_charac))
    msg_out = bytearray(msg_in)
    if erase_pos is None:
        erase_pos = []
    else:
        for e_pos in erase_pos:
            msg_out[e_pos] = 0
    if len(erase_pos) > nsym:
        raise ReedSolomonError('Too many erasures to correct')
    synd = rs_calc_syndromes(msg_out, nsym, fcr, generator)
    if max(synd) == 0:
        return msg_out[:-nsym], msg_out[-nsym:]
    erase_loc = None
    erase_count = 0
    if erase_pos:
        erase_count = len(erase_pos)
        erase_pos_reversed = [(len(msg_out) - 1 - eras) for eras in erase_pos]
        erase_loc = rs_find_errata_locator(erase_pos_reversed, generator=
            generator)
    if only_erasures:
        err_loc = erase_loc[::-1]
    else:
        err_loc = rs_find_error_locator(synd, nsym, erase_loc=erase_loc,
            erase_count=erase_count)
        err_loc = err_loc[::-1]
    err_pos = rs_find_errors(err_loc, len(msg_out), generator)
    if err_pos is None:
        raise ReedSolomonError('Could not locate error')
    msg_out = rs_correct_errata(msg_out, synd, err_pos, fcr=fcr, generator=
        generator)
    synd = rs_calc_syndromes(msg_out, nsym, fcr, generator)
    if max(synd) > 0:
        raise ReedSolomonError('Could not correct message')
    return msg_out[:-nsym], msg_out[-nsym:]