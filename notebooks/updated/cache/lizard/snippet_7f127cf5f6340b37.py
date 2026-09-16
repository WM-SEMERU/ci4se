def renderHTTP(self, ctx):
    req = inevow.IRequest(ctx)
    if req.method == 'POST':
        udata = req.fields['uploaddata']
        self.cbGotMugshot(udata.type.decode('ascii'), udata.file)
    return rend.Page.renderHTTP(self, ctx)