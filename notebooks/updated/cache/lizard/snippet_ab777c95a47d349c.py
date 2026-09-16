def turn_on(host, did, token=None):
    urllib3.disable_warnings()
    if token:
        scheme = 'https'
    if not token:
        scheme = 'http'
        token = '1234567890'
    url = (scheme + '://' + host +
        '/gwr/gop.php?cmd=DeviceSendCommand&data=<gip><version>1</version><token>'
         + token + '</token><did>' + did +
        '</did><value>1</value></gip>&fmt=xml')
    response = requests.get(url, verify=False)
    if response.status_code == '200':
        return True
    else:
        return False