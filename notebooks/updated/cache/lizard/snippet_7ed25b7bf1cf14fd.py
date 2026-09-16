def addfield(self, name, type, width=10):
    fieldDefn = ogr.FieldDefn(name, type)
    if type == ogr.OFTString:
        fieldDefn.SetWidth(width)
    self.layer.CreateField(fieldDefn)