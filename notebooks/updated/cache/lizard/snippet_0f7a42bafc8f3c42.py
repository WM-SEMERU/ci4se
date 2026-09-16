def validate_scopes(value_list):
    for value in value_list:
        if value not in current_oauth2server.scopes:
            raise ScopeDoesNotExists(value)
    return True