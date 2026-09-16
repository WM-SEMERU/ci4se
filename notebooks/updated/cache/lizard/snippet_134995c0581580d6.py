def display_iframe_url(target, **kwargs):
    txt = iframe_url(target, **kwargs)
    display(HTML(txt))