async def get_users(self, include_disabled=False):
    client_facade = client.UserManagerFacade.from_connection(self.connection())
    response = await client_facade.UserInfo(None, include_disabled)
    return [User(self, r.result) for r in response.results]