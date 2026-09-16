def compile_validation_pattern(self, units=None):
    if units is None:
        units = list(self.POSSIBLE_UNITS)
    else:
        for u in units:
            if u not in self.POSSIBLE_UNITS:
                raise ValidationError('{} is not a valid unit for a size field'
                    .format(u))
    regex = re.compile('^(-?\\d+)({})$'.format('|'.join(units)))
    endings = (' %s ' % ugettext('or')).join("'%s'" % u.replace('%', '%%') for
        u in units)
    params = {'label': '%(label)s', 'value': '%(value)s', 'field':
        '%(field)s', 'endings': endings}
    return regex, self.invalid_message % params