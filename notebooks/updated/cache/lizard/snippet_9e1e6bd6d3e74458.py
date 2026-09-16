def getstr_data(self, name, vals):
    fld2val = self.get_fld2val(name, vals)
    return self.fmt.format(**fld2val)