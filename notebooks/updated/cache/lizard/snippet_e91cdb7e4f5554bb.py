def show_weights(estimator, **kwargs):
    format_kwargs, explain_kwargs = _split_kwargs(kwargs)
    expl = explain_weights(estimator, **explain_kwargs)
    html = format_as_html(expl, **format_kwargs)
    return HTML(html)