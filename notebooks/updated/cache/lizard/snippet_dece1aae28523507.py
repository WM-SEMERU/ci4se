def tj_email(self):
    for email in self.emails.all():
        if email.address.endswith(('@fcps.edu', '@tjhsst.edu')):
            return email
    if self.is_teacher:
        domain = 'fcps.edu'
    else:
        domain = 'tjhsst.edu'
    return '{}@{}'.format(self.username, domain)