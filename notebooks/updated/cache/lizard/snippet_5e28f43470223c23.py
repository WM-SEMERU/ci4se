def check_connection(self):
    nntpserver = self.host or self.aggregate.config['nntpserver']
    if not nntpserver:
        self.add_warning(_(
            'No NNTP server was specified, skipping this URL.'), tag=
            WARN_NNTP_NO_SERVER)
        return
    nntp = self._connect_nntp(nntpserver)
    group = self.urlparts[2]
    while group[:1] == '/':
        group = group[1:]
    if '@' in group:
        number = nntp.stat('<' + group + '>')[1]
        self.add_info(_('Article number %(num)s found.') % {'num': number})
    else:
        group = group.split('/', 1)[0]
        if group:
            name = nntp.group(group)[4]
            self.add_info(_('News group %(name)s found.') % {'name': name})
        else:
            self.add_warning(_('No newsgroup specified in NNTP URL.'), tag=
                WARN_NNTP_NO_NEWSGROUP)