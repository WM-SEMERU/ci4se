def get_stats_display_height(self, curse_msg):
    r
    try:
        c = [i['msg'] for i in curse_msg['msgdict']].count('\n')
    except Exception as e:
        logger.debug('ERROR: Can not compute plugin height ({})'.format(e))
        return 0
    else:
        return c + 1