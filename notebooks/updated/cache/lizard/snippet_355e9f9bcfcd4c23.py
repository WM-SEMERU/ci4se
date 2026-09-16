def register_for_duty(self, context):
    cctxt = self.client.prepare()
    return cctxt.call(context, 'register_for_duty', host=self.host)