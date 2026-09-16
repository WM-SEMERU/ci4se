def check_robotstxt(url, session):
    roboturl = get_roboturl(url)
    rp = get_robotstxt_parser(roboturl, session=session)
    if not rp.can_fetch(UserAgent, str(url)):
        raise IOError('%s is disallowed by %s' % (url, roboturl))