def check_signature(params):
    if 'id' in params:
        try:
            id_int = int(params['id'][0])
        except:
            my_log_message(args, syslog.LOG_INFO, 
                'Non-numerical client id (%s) in request.' % params['id'][0])
            return False, None
        key = client_ids.get(id_int)
        if key:
            if 'h' in params:
                sig = params['h'][0]
                good_sig = make_signature(params, key)
                if sig == good_sig:
                    return True, key
                else:
                    my_log_message(args, syslog.LOG_INFO, 
                        "Bad signature from client id '%i' (%s, expected %s)."
                         % (id_int, sig, good_sig))
            else:
                my_log_message(args, syslog.LOG_INFO, 
                    'Client id (%i) but no HMAC in request.' % id_int)
                return False, key
        else:
            my_log_message(args, syslog.LOG_INFO, "Unknown client id '%i'" %
                id_int)
            return False, None
    return True, None