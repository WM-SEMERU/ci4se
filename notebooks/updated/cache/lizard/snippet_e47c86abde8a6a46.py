def get_ip_scope(auth, url, scopeid=None):
    if scopeid is None:
        get_ip_scope_url = '/imcrs/res/access/assignedIpScope'
    else:
        get_ip_scope_url = (
            '/imcrs/res/access/assignedIpScope/ip?ipScopeId=' + str(scopeid))
    f_url = url + get_ip_scope_url
    response = requests.get(f_url, auth=auth, headers=HEADERS)
    try:
        if response.status_code == 200:
            ipscopelist = json.loads(response.text)['assignedIpScope']
            if isinstance(ipscopelist, list):
                return ipscopelist
            elif isinstance(ipscopelist, dict):
                return [ipscopelist]
    except requests.exceptions.RequestException as error:
        return 'Error:\n' + str(error) + ' get_ip_scope: An Error has occured'