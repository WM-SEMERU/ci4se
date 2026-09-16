def __GetAuthorizationTokenUsingResourceTokens(resource_tokens, path,
    resource_id_or_fullname):
    if resource_tokens and len(resource_tokens) > 0:
        if not path and not resource_id_or_fullname:
            return next(six.itervalues(resource_tokens))
        if resource_tokens.get(resource_id_or_fullname):
            return resource_tokens[resource_id_or_fullname]
        else:
            path_parts = []
            if path:
                path_parts = path.split('/')
            resource_types = ['dbs', 'colls', 'docs', 'sprocs', 'udfs',
                'triggers', 'users', 'permissions', 'attachments', 'media',
                'conflicts', 'offers']
            for one_part in reversed(path_parts):
                if (not one_part in resource_types and one_part in
                    resource_tokens):
                    return resource_tokens[one_part]
    return None