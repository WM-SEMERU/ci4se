async def get(self, request):
    form = await self.get_form(request)
    ctx = dict(active=self, form=form, request=request)
    if self.resource:
        return self.app.ps.jinja2.render(self.template_item, **ctx)
    return self.app.ps.jinja2.render(self.template_list, **ctx)