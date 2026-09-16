def _deserialize(self, value, attr, obj):
    if value is None:
        return None
    try:
        return float(value)
    except ValueError:
        parsed = parser.parse(value)
        if parsed.tzinfo:
            if parsed.utcoffset().total_seconds():
                raise ValidationError('Timestamps must be defined in UTC')
            parsed = parsed.replace(tzinfo=None)
        return (parsed - TimestampField.EPOCH).total_seconds()