def from_dict(cls, dic):
    if '__version__' not in dic:
        raise ValueError('Not support old docpie data')
    data_version = int(dic['__version__'].replace('.', ''))
    this_version = int(cls._version.replace('.', ''))
    logger.debug('this: %s, old: %s', this_version, data_version)
    if data_version < this_version:
        raise ValueError('Not support old docpie data')
    assert dic['__class__'] == 'Docpie'
    config = dic['__config__']
    help = config.pop('help')
    version = config.pop('version')
    option_name = config.pop('option_name')
    usage_name = config.pop('usage_name')
    self = cls(None, **config)
    self.option_name = option_name
    self.usage_name = usage_name
    text = dic['__text__']
    self.doc = text['doc']
    self.usage_text = text['usage_text']
    self.option_sections = text['option_sections']
    self.opt_names = [set(x) for x in dic['option_names']]
    self.opt_names_required_max_args = dic['opt_names_required_max_args']
    self.set_config(help=help, version=version)
    self.options = o = {}
    for title, options in dic['option'].items():
        opt_ins = [convert_2_object(x, {}, self.namedoptions) for x in options]
        o[title] = opt_ins
    self.usages = [convert_2_object(x, self.options, self.namedoptions) for
        x in dic['usage']]
    return self