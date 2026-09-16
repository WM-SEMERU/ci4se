def by_zipcode(self, zipcode, zipcode_type=None, zero_padding=True):
    if zero_padding:
        zipcode = str(zipcode).zfill(5)
    else:
        zipcode = str(zipcode)
    res = self.query(zipcode=zipcode, sort_by=None, returns=1, zipcode_type
        =zipcode_type)
    if len(res):
        return res[0]
    else:
        return self.zip_klass()