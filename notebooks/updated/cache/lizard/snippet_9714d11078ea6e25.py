def ulocalized_gmt0_time(self, time, context, request):
    value = get_date(context, time)
    if not value:
        return ''
    value = value.toZone('GMT+0')
    return self.ulocalized_time(value, context, request)