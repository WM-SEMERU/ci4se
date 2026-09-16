def fill_addressfields(self, row, obj):
    addresses = {}
    for add_type in ['Physical', 'Postal', 'Billing', 'CountryState']:
        addresses[add_type] = {}
        for key in ['Address', 'City', 'State', 'District', 'Zip', 'Country']:
            addresses[add_type][key.lower()] = str(row.get('%s_%s' % (
                add_type, key), ''))
    if addresses['CountryState']['country'] == '' and addresses['CountryState'
        ]['state'] == '':
        addresses['CountryState']['country'] = addresses['Physical']['country']
        addresses['CountryState']['state'] = addresses['Physical']['state']
    if hasattr(obj, 'setPhysicalAddress'):
        obj.setPhysicalAddress(addresses['Physical'])
    if hasattr(obj, 'setPostalAddress'):
        obj.setPostalAddress(addresses['Postal'])
    if hasattr(obj, 'setCountryState'):
        obj.setCountryState(addresses['CountryState'])
    if hasattr(obj, 'setBillingAddress'):
        obj.setBillingAddress(addresses['Billing'])