def _lab_data(self):
    portal = self.context.portal_url.getPortalObject()
    lab = self.context.bika_setup.laboratory
    lab_address = lab.getPostalAddress() or lab.getBillingAddress(
        ) or lab.getPhysicalAddress()
    if lab_address:
        _keys = ['address', 'city', 'state', 'zip', 'country']
        _list = [('<div>%s</div>' % lab_address.get(v)) for v in _keys if
            lab_address.get(v)]
        lab_address = ''.join(_list)
    else:
        lab_address = ''
    return {'obj': lab, 'title': to_utf8(lab.Title()), 'url': to_utf8(lab.
        getLabURL()), 'address': to_utf8(lab_address), 'confidence': lab.
        getConfidence(), 'accredited': lab.getLaboratoryAccredited(),
        'accreditation_body': to_utf8(lab.getAccreditationBody()),
        'accreditation_logo': lab.getAccreditationBodyLogo(), 'logo': 
        '%s/logo_print.png' % portal.absolute_url()}