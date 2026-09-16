def setup(name, path='log', enable_debug=False):
    path_tmpl = os.path.join(path, '{name}_{level}.log')
    info = path_tmpl.format(name=name, level='info')
    warn = path_tmpl.format(name=name, level='warn')
    err = path_tmpl.format(name=name, level='err')
    crit = path_tmpl.format(name=name, level='crit')
    setup = [NullHandler(), TimedRotatingFileHandler(info, level='INFO',
        encoding='utf-8', date_format='%Y-%m-%d'), TimedRotatingFileHandler
        (warn, level='WARNING', encoding='utf-8', date_format='%Y-%m-%d'),
        TimedRotatingFileHandler(err, level='ERROR', encoding='utf-8',
        date_format='%Y-%m-%d'), TimedRotatingFileHandler(crit, level=
        'CRITICAL', encoding='utf-8', date_format='%Y-%m-%d')]
    if enable_debug:
        debug = path_tmpl.format(name=name, level='debug')
        setup.insert(1, TimedRotatingFileHandler(debug, level='DEBUG',
            encoding='utf-8', date_format='%Y-%m-%d'))
    if (src_server is not None and smtp_server is not None and smtp_port !=
        0 and len(dest_mails) != 0):
        mail_tmpl = '{name}_error@{src}'
        from_mail = mail_tmpl.format(name=name, src=src_server)
        subject = 'Error in {}'.format(name)
        setup.append(MailHandler(from_mail, dest_mails, subject, level=
            'ERROR', bubble=True, server_addr=(smtp_server, smtp_port)))
    return NestedSetup(setup)