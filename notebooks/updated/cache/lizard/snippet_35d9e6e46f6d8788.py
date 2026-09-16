def location(ip=None, key=None, field=None):
    if field and field not in field_list:
        return 'Invalid field'
    if field:
        if ip:
            url = 'https://ipapi.co/{}/{}/'.format(ip, field)
        else:
            url = 'https://ipapi.co/{}/'.format(field)
    elif ip:
        url = 'https://ipapi.co/{}/json/'.format(ip)
    else:
        url = 'https://ipapi.co/json/'
    if key or API_KEY:
        url = '{}?key={}'.format(url, key or API_KEY)
    response = get(url, headers=headers)
    if field:
        return response.text
    else:
        return response.json()