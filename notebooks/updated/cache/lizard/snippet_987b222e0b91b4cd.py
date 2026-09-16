def SetDefaultValue(self, scan_object):
    if not isinstance(scan_object, PathFilterScanTreeNode) and not isinstance(
        scan_object, py2to3.STRING_TYPES):
        raise TypeError('Unsupported scan object type.')
    if self.default_value:
        raise ValueError('Default value already set.')
    self.default_value = scan_object