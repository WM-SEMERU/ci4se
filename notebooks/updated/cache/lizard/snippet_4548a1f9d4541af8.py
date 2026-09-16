def get_template_names(self):
    posted_name = self.request.POST.get('template_name')
    if posted_name:
        return [posted_name]
    else:
        return super(PagePreviewView, self).get_template_names()