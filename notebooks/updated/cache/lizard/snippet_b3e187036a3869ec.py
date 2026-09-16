async def get_user(self, username, secret_key=None):
    client_facade = client.UserManagerFacade.from_connection(self.connection())
    user = tag.user(username)
    args = [client.Entity(user)]
    try:
        response = await client_facade.UserInfo(args, True)
    except errors.JujuError as e:
        if 'permission denied' in e.errors:
            return None
        raise
    if response.results and response.results[0].result:
        return User(self, response.results[0].result, secret_key=secret_key)
    return None