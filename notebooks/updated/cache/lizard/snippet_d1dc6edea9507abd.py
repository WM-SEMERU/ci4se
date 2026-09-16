def alarm(cls, template, default_params={}, stack_depth=0, log_context=None,
    **more_params):
    timestamp = datetime.utcnow()
    format = '*' * 80 + CR + indent(template, prefix='** ').strip(
        ) + CR + '*' * 80
    Log._annotate(LogItem(context=exceptions.ALARM, format=format, template
        =template, params=dict(default_params, **more_params)), timestamp, 
        stack_depth + 1)