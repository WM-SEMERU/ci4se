async def get(self, public_key):
    if settings.SIGNATURE_VERIFICATION:
        super().verify()
    response = await self.account.getnews(public_key=public_key)
    if isinstance(response, list):
        self.write(json.dumps(response))
        raise tornado.web.Finish
    elif isinstance(response, dict):
        try:
            error_code = response['error']
        except:
            del response['account_id']
            self.write(response)
        else:
            self.set_status(error_code)
            self.write(response)
            raise tornado.web.Finish