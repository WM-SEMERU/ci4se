def python_date_format(self, long_format=None, time_only=False):
    msgid = long_format and 'date_format_long' or 'date_format_short'
    if time_only:
        msgid = 'time_format'
    formatstring = translate(msgid, domain='senaite.core', context=self.request
        )
    if formatstring is None or formatstring.startswith('date_'
        ) or formatstring.startswith('time_'):
        self.logger.error('bika/%s/%s could not be translated' % (self.
            request.get('LANGUAGE'), msgid))
        properties = getToolByName(self.context, 'portal_properties'
            ).site_properties
        if long_format:
            format = properties.localLongTimeFormat
        elif time_only:
            format = properties.localTimeOnlyFormat
        else:
            format = properties.localTimeFormat
        return format
    return formatstring.replace('${', '%').replace('}', '')