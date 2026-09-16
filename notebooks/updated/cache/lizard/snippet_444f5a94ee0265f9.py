def ToJson(self):
    jsn = super(InvocationTransaction, self).ToJson()
    jsn['script'] = self.Script.hex()
    jsn['gas'] = self.Gas.ToNeoJsonString()
    return jsn