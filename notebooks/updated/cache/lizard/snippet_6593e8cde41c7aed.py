def parseCustom(self, xbrl, ignore_errors=0):
    custom_obj = Custom()
    custom_data = xbrl.find_all(re.compile(
        '^((?!(us-gaap|dei|xbrll|xbrldi)).)*:\\s*', re.IGNORECASE | re.
        MULTILINE))
    elements = {}
    for data in custom_data:
        if XBRLParser().is_number(data.text):
            setattr(custom_obj, data.name.split(':')[1], data.text)
    return custom_obj