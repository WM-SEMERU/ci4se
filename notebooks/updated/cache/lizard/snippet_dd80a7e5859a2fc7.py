def enforce_filetype_file(form, field):
    if form._fields.get('filetype').data != RESOURCE_FILETYPE_FILE:
        return
    domain = urlparse(field.data).netloc
    allowed_domains = current_app.config['RESOURCES_FILE_ALLOWED_DOMAINS']
    allowed_domains += [current_app.config.get('SERVER_NAME')]
    if current_app.config.get('CDN_DOMAIN'):
        allowed_domains.append(current_app.config['CDN_DOMAIN'])
    if '*' in allowed_domains:
        return
    if domain and domain not in allowed_domains:
        message = _('Domain "{domain}" not allowed for filetype "{filetype}"')
        raise validators.ValidationError(message.format(domain=domain,
            filetype=RESOURCE_FILETYPE_FILE))