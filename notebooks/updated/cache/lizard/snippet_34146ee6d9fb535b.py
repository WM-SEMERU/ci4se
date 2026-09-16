def format_output(self, rendered_widgets):
    rendered = super(KeywordsWidget, self).format_output(rendered_widgets)
    links = ''
    for keyword in Keyword.objects.all().order_by('title'):
        prefix = '+' if str(keyword.id) not in self._ids else '-'
        links += "<a href='#'>%s%s</a>" % (prefix, str(keyword))
    rendered += mark_safe("<p class='keywords-field'>%s</p>" % links)
    return rendered