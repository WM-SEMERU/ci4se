def get_email(self, token):
    resp = requests.get(self.emails_url, params={'access_token': token.token})
    emails = resp.json().get('values', [])
    email = ''
    try:
        email = emails[0].get('email')
        primary_emails = [e for e in emails if e.get('is_primary', False)]
        email = primary_emails[0].get('email')
    except (IndexError, TypeError, KeyError):
        return ''
    finally:
        return email