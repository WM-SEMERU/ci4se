def _parse_date_rfc822(dateString):
    data = dateString.split()
    if data[0][-1] in (',', '.') or data[0].lower() in rfc822._daynames:
        del data[0]
    if len(data) == 4:
        s = data[3]
        i = s.find('+')
        if i > 0:
            data[3:] = [s[:i], s[i + 1:]]
        else:
            data.append('')
        dateString = ' '.join(data)
    if len(data) < 5:
        dateString += ' 00:00:00 GMT'
    return rfc822.parsedate_tz(dateString)