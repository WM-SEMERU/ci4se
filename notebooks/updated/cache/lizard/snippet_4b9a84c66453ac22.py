def body_class_tag(context):
    request = context.get('request')
    if not hasattr(request, 'ROUTE'):
        return ''
    css_classes = []
    namespace = request.ROUTE['namespace']
    if namespace:
        namespace = RE_CLEAN_CSS_NAME.sub('-', namespace.lower())
        css_classes.append('ns-{}'.format(namespace))
    view = request.ROUTE['url_name']
    if view:
        view = RE_CLEAN_CSS_NAME.sub('-', view.lower())
        css_classes.append('vw-{}'.format(view))
    return ' '.join(css_classes)