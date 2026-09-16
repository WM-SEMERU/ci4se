def rs_simple_encode_msg(msg_in, nsym, fcr=0, generator=2, gen=None):
    global field_charac
    if len(msg_in) + nsym > field_charac:
        raise ValueError('Message is too long (%i when max is %i)' % (len(
            msg_in) + nsym, field_charac))
    if gen is None:
        gen = rs_generator_poly(nsym, fcr, generator)
    _, remainder = gf_poly_div(msg_in + bytearray(len(gen) - 1), gen)
    msg_out = msg_in + remainder
    return msg_out