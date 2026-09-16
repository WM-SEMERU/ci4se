def fn_getdatetime_list(fn):
    fn = os.path.split(os.path.splitext(fn)[0])[-1]
    import re
    dstr = None
    out = None
    dstr = re.findall(
        '(?:^|_|-)(?:19|20)[0-9][0-9](?:0[1-9]|1[012])(?:0[1-9]|[12][0-9]|3[01])[_T](?:0[0-9]|1[0-9]|2[0-3])[0-5][0-9]'
        , fn)
    if not dstr:
        dstr = re.findall(
            '(?:^|_|-)(?:19|20)[0-9][0-9](?:0[1-9]|1[012])(?:0[1-9]|[12][0-9]|3[01])(?:0[0-9]|1[0-9]|2[0-3])[0-5][0-9]'
            , fn)
    if not dstr:
        dstr = re.findall(
            '(?:^|_|-)(?:19|20)[0-9][0-9](?:0[1-9]|1[012])(?:0[1-9]|[12][0-9]|3[01])(?:$|_|-)'
            , fn)
    if not dstr:
        dstr = re.findall(
            '(?:^|_|-)(?:19|20)[0-9][0-9]\\.[0-9][0-9][0-9]*(?:$|_|-)', fn)
        dstr = [d.lstrip('_').rstrip('_') for d in dstr]
        dstr = [d.lstrip('-').rstrip('-') for d in dstr]
        out = [decyear2dt(float(s)) for s in dstr]
        dstr = None
    if not dstr:
        dstr = re.findall('(?:^|_|-)(?:19|20)[0-9][0-9](?:$|_|-)', fn)
    if not dstr:
        dstr = re.findall('[0-3][0-9][a-z][a-z][a-z][0-9][0-9]', fn)
        if dstr:
            out = [datetime.strptime(s, '%d%b%y') for s in dstr][0]
            dstr = None
    if dstr:
        dstr = [d.lstrip('_').rstrip('_') for d in dstr]
        dstr = [d.lstrip('-').rstrip('-') for d in dstr]
        out = [strptime_fuzzy(s) for s in dstr]
    return out