def createEmails(nicks=None, nicksFile=None):
    candidate_emails = set()
    if nicks != None:
        for n in nicks:
            for e in email_providers.domains:
                candidate_emails.add('{}@{}'.format(n, e))
    elif nicksFile != None:
        with open(nicksFile, 'r') as iF:
            nicks = iF.read().splitlines()
            for n in nicks:
                for e in email_providers.domains:
                    candidate_emails.add('{}@{}'.format(n, e))
    return candidate_emails