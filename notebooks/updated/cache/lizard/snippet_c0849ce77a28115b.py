async def delete(cls, access_key: str):
    q = (
        'mutation($access_key: String!) {  delete_keypair(access_key: $access_key) {    ok msg  }}'
        )
    variables = {'access_key': access_key}
    rqst = Request(cls.session, 'POST', '/admin/graphql')
    rqst.set_json({'query': q, 'variables': variables})
    async with rqst.fetch() as resp:
        data = await resp.json()
        return data['delete_keypair']