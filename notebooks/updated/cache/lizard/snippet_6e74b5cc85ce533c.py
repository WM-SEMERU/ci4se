def get_stats_display_width(self, curse_msg, without_option=False):
    try:
        if without_option:
            c = len(max(''.join([(u(u(nativestr(i['msg'])).encode('ascii',
                'replace')) if not i['optional'] else '') for i in
                curse_msg['msgdict']]).split('\n'), key=len))
        else:
            c = len(max(''.join([u(u(nativestr(i['msg'])).encode('ascii',
                'replace')) for i in curse_msg['msgdict']]).split('\n'),
                key=len))
    except Exception as e:
        logger.debug('ERROR: Can not compute plugin width ({})'.format(e))
        return 0
    else:
        return c