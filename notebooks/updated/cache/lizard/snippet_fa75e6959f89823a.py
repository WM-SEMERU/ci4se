def restore(self, value, context=None):
    context = context or orb.Context()
    value = super(ReferenceColumn, self).restore(value, context=context)
    if self.testFlag(self.Flags.I18n) and context.locale == 'all':
        return {locale: self._restore(val, context) for locale, val in
            value.items()}
    else:
        return self._restore(value, context)