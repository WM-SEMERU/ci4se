def valid_email(emailaddress, domains=GENERIC_DOMAINS):
    if len(emailaddress) < 6:
        return False
    try:
        localpart, domainname = emailaddress.rsplit('@', 1)
        host, toplevel = domainname.rsplit('.', 1)
    except ValueError:
        return False
    if len(toplevel) != 2 and toplevel not in domains:
        return False
    for i in '-_.%+.':
        localpart = localpart.replace(i, '')
    for i in '-_.':
        host = host.replace(i, '')
    if localpart.isalnum() and host.isalnum():
        return True
    else:
        return False