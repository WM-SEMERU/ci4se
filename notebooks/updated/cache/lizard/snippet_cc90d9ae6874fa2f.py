async def reset_user_password(self, username):
    user_facade = client.UserManagerFacade.from_connection(self.connection())
    entity = client.Entity(tag.user(username))
    results = await user_facade.ResetPassword([entity])
    secret_key = results.results[0].secret_key
    return await self.get_user(username, secret_key=secret_key)