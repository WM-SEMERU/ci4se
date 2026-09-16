def date_0utc(date):
    return ee.Date.fromYMD(date.get('year'), date.get('month'), date.get('day')
        )