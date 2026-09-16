def __get_ssl_context(cls, sslca=None):
    if version_info[0] == 2 and (version_info[1] >= 7 and version_info[2] >= 5
        ) or version_info[0] == 3 and version_info[1] >= 4:
        logger.debug('SSL method for 2.7.5+ / 3.4+')
        from ssl import SSLContext, PROTOCOL_TLSv1_2, CERT_REQUIRED, OP_NO_COMPRESSION
        ctx = SSLContext(PROTOCOL_TLSv1_2)
        ctx.set_ciphers('HIGH:!SSLv3:!TLSv1:!aNULL:@STRENGTH')
        ctx.options |= OP_NO_COMPRESSION
        if sslca:
            ctx.load_verify_locations(sslca)
            ctx.verify_mode = CERT_REQUIRED
            ctx.check_hostname = False
        else:
            from ssl import Purpose
            ctx.load_default_certs(purpose=Purpose.SERVER_AUTH)
            ctx.verify_mode = CERT_REQUIRED
            ctx.check_hostname = True
    elif version_info[0] == 3 and version_info[1] < 4:
        logger.debug('Using SSL method for 3.2+, < 3.4')
        from ssl import SSLContext, CERT_REQUIRED, PROTOCOL_SSLv23, OP_NO_SSLv2, OP_NO_SSLv3, OP_NO_TLSv1
        ctx = SSLContext(PROTOCOL_SSLv23)
        ctx.options |= OP_NO_SSLv2 | OP_NO_SSLv3 | OP_NO_TLSv1
        ctx.set_ciphers('HIGH:!SSLv3:!TLSv1:!aNULL:@STRENGTH')
        if sslca:
            ctx.load_verify_locations(sslca)
            ctx.verify_mode = CERT_REQUIRED
        else:
            ctx.set_default_verify_paths()
            ctx.verify_mode = CERT_REQUIRED
    else:
        raise Exception('Unsupported Python version %s' % '.'.join(str(item
            ) for item in version_info[:3]))
    return ctx