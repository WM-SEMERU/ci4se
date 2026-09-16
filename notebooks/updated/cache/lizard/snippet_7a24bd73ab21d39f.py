async def add_user(self, username, password=None, display_name=None):
    if not display_name:
        display_name = username
    user_facade = client.UserManagerFacade.from_connection(self.connection())
    users = [client.AddUser(display_name=display_name, username=username,
        password=password)]
    results = await user_facade.AddUser(users)
    secret_key = results.results[0].secret_key
    return await self.get_user(username, secret_key=secret_key)