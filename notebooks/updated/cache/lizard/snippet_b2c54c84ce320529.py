def _printedby_data(self, ws):
    data = {}
    member = self.context.portal_membership.getAuthenticatedMember()
    if member:
        username = member.getUserName()
        data['username'] = username
        data['fullname'] = to_utf8(self.user_fullname(username))
        data['email'] = to_utf8(self.user_email(username))
        c = [x for x in self.bika_setup_catalog(portal_type='LabContact') if
            x.getObject().getUsername() == username]
        if c:
            sf = c[0].getObject().getSignature()
            if sf:
                data['signature'] = sf.absolute_url() + '/Signature'
    return data