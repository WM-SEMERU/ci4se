def render_icon(icon, **kwargs):
    attrs = {'class': add_css_class('glyphicon glyphicon-{icon}'.format(
        icon=icon), kwargs.get('extra_classes', ''))}
    title = kwargs.get('title')
    if title:
        attrs['title'] = title
    return render_tag('span', attrs=attrs)