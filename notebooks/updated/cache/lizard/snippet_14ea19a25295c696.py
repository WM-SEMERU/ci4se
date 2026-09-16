async def disable_user(self, username):
    user_facade = client.UserManagerFacade.from_connection(self.connection())
    entity = client.Entity(tag.user(username))
    return await user_facade.DisableUser([entity])