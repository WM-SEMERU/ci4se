def is_js_date_utc(json):
    JS_date_utc_pattern = (
        'Date\\.UTC\\(([0-9]+,[0-9]+,[0-9]+)(,[0-9]+,[0-9]+,[0-9]+)?(,[0-9]+)?\\)'
        )
    re_date = re.compile(JS_date_utc_pattern, re.M)
    if re_date.search(json):
        return re_date.search(json).group(0)
    else:
        return False