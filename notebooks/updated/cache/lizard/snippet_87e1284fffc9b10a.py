def from_config(config):
    debug_mode = config.get('mode') == 'debug'
    name = config.get('recruiter', None)
    recruiter = None
    if config.get('replay'):
        return HotAirRecruiter()
    if name is not None:
        recruiter = by_name(name)
        if isinstance(recruiter, (BotRecruiter, MultiRecruiter)):
            return recruiter
    if debug_mode:
        return HotAirRecruiter()
    if recruiter is not None:
        return recruiter
    if name and recruiter is None:
        raise NotImplementedError('No such recruiter {}'.format(name))
    return MTurkRecruiter()