def ServiceAccountCredentialsFromFile(filename, scopes, user_agent=None):
    filename = os.path.expanduser(filename)
    if oauth2client.__version__ > '1.5.2':
        credentials = (service_account.ServiceAccountCredentials.
            from_json_keyfile_name(filename, scopes=scopes))
        if credentials is not None:
            if user_agent is not None:
                credentials.user_agent = user_agent
        return credentials
    else:
        with open(filename) as keyfile:
            service_account_info = json.load(keyfile)
        account_type = service_account_info.get('type')
        if account_type != oauth2client.client.SERVICE_ACCOUNT:
            raise exceptions.CredentialsError(
                'Invalid service account credentials: %s' % (filename,))
        credentials = service_account._ServiceAccountCredentials(
            service_account_id=service_account_info['client_id'],
            service_account_email=service_account_info['client_email'],
            private_key_id=service_account_info['private_key_id'],
            private_key_pkcs8_text=service_account_info['private_key'],
            scopes=scopes, user_agent=user_agent)
        return credentials