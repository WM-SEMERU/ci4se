def read_properties(filename):
    s = path(filename).text()
    dummy_section = 'xxx'
    cfgparser = configparser.RawConfigParser()
    cfgparser.optionxform = str
    cfgparser.readfp(StringIO('[%s]\n' % dummy_section + s))
    bunch = AutoBunch()
    for x in cfgparser.options(dummy_section):
        setattr(bunch, x, cfgparser.get(dummy_section, str(x)))
    return bunch