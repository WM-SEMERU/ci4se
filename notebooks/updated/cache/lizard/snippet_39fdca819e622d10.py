def sendEmail(self, emails, mass_type='SingleEmailMessage'):
    preparedEmails = _prepareSObjects(emails)
    if isinstance(preparedEmails, dict):
        del preparedEmails['fieldsToNull']
    else:
        for listitems in preparedEmails:
            del listitems['fieldsToNull']
    res = BaseClient.sendEmail(self, preparedEmails, mass_type)
    if type(res) not in (TupleType, ListType):
        res = [res]
    data = list()
    for resu in res:
        d = dict()
        data.append(d)
        d['success'] = success = _bool(resu[_tPartnerNS.success])
        if not success:
            d['errors'] = [_extractError(e) for e in resu[_tPartnerNS.errors,]]
        else:
            d['errors'] = list()
    return data