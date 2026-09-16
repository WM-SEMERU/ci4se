def checklink(form=None, env=os.environ):
    if form is None:
        form = {}
    try:
        checkform(form, env)
    except LCFormError as errmsg:
        log(env, errmsg)
        yield encode(format_error(errmsg))
        return
    out = ThreadsafeIO()
    config = get_configuration(form, out)
    url = strformat.stripurl(formvalue(form, 'url'))
    aggregate = director.get_aggregate(config)
    url_data = checker.get_url_from(url, 0, aggregate, extern=(0, 0))
    aggregate.urlqueue.put(url_data)
    for html_str in start_check(aggregate, out):
        yield encode(html_str)
    out.close()