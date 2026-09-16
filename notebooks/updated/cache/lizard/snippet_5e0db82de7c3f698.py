def generate(self, *args, **kwargs):
    title = kwargs.get('title')
    heads = kwargs.get('heads')
    refresh = kwargs.get('refresh')
    filename = args[0]
    report = self._create(title, heads, refresh, path_start=os.path.dirname
        (filename))
    ReportHtml.save(report, filename)