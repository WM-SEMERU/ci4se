def Parse(self, stat, unused_knowledge_base):
    value = stat.registry_data.GetValue()
    if not str(value).isdigit() or int(value) > 999 or int(value) < 0:
        raise parser.ParseError(
            'Invalid value for CurrentControlSet key %s' % value)
    yield rdfvalue.RDFString('HKEY_LOCAL_MACHINE\\SYSTEM\\ControlSet%03d' %
        int(value))