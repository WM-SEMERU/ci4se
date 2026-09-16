def pdfa_status(self):
    key_part = QName(XMP_NS_PDFA_ID, 'part')
    key_conformance = QName(XMP_NS_PDFA_ID, 'conformance')
    try:
        return self[key_part] + self[key_conformance]
    except KeyError:
        return ''