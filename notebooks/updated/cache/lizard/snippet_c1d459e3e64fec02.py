def image(radar, at=None):
    at = round_to_5_minutes(at or datetime.utcnow())
    return ''.join(['http://image.nmc.cn/product', '/{0}'.format(at.year),
        '/{0}'.format(at.strftime('%Y%m')), '/{0}'.format(at.strftime(
        '%Y%m%d')), '/RDCP/medium/SEVP_AOC_RDCP_SLDAS_EBREF_',
        '{0}_L88_PI_'.format(radar), '{0}00000.GIF'.format(at.strftime(
        '%Y%m%d%H%M'))])