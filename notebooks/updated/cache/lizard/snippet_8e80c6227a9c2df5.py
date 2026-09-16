def _fields_valid(self, d):
    if 'DATATYPE' not in d:
        return False
    datatype = d['DATATYPE']
    if datatype == 'HOSTPERFDATA':
        fields = self.GENERIC_FIELDS + self.HOST_FIELDS
    elif datatype == 'SERVICEPERFDATA':
        fields = self.GENERIC_FIELDS + self.SERVICE_FIELDS
    else:
        return False
    for field in fields:
        if field not in d:
            return False
    return True