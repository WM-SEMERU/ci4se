def check_mailfy(self, query, kwargs={}):
    import requests
    s = requests.Session()
    r1 = s.get('https://www.infojobs.net')
    r2 = s.post(
        'https://www.infojobs.net/candidate/profile/check-email-registered.xhtml'
        , data={'email': query})
    if '{"email_is_secure":true,"email":true}' in r2.text:
        return r2.text
    return None