def set_config_modify(dn=None, inconfig=None, hierarchical=False):
    ret = {}
    cookie = logon()
    h = 'false'
    if hierarchical is True:
        h = 'true'
    payload = (
        '<configConfMo cookie="{0}" inHierarchical="{1}" dn="{2}"><inConfig>{3}</inConfig></configConfMo>'
        .format(cookie, h, dn, inconfig))
    r = __utils__['http.query'](DETAILS['url'], data=payload, method='POST',
        decode_type='plain', decode=True, verify_ssl=False, raise_error=
        True, status=True, headers=DETAILS['headers'])
    _validate_response_code(r['status'], cookie)
    answer = re.findall('(<[\\s\\S.]*>)', r['text'])[0]
    items = ET.fromstring(answer)
    logout(cookie)
    for item in items:
        ret[item.tag] = prepare_return(item)
    return ret