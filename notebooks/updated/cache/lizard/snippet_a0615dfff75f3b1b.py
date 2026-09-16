def mail_container(value):
    if not re.match('.*://.*', value):
        raise VdtTypeError(value)
    mburl = urlparse(value)
    uri_scheme_to_mbclass = {'mbox': mailbox.mbox, 'maildir': mailbox.
        Maildir, 'mh': mailbox.MH, 'babyl': mailbox.Babyl, 'mmdf': mailbox.MMDF
        }
    klass = uri_scheme_to_mbclass.get(mburl.scheme)
    if klass:
        return klass(mburl.netloc + mburl.path)
    raise VdtTypeError(value)