async def fetch_invite(self, url, *, with_counts=True):
    invite_id = utils.resolve_invite(url)
    data = await self.http.get_invite(invite_id, with_counts=with_counts)
    return Invite.from_incomplete(state=self._connection, data=data)