def bootstrap_javascript(jquery=None):
    javascript = ''
    if jquery is None:
        jquery = get_bootstrap_setting('include_jquery', False)
    if jquery:
        url = bootstrap_jquery_url()
        if url:
            javascript += render_script_tag(url)
    url = bootstrap_javascript_url()
    if url:
        javascript += render_script_tag(url)
    return mark_safe(javascript)