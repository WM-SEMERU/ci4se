def profiling_request_formatter(view, context, model, name):
    document = model[name]
    return Markup(''.join(['<p class="profiling-request">', '<a href="{}">'
        .format(document.get_admin_url(_external=True)),
        http_method_formatter(view, context, document, 'method'), '&nbsp;',
        document.path, '</a>', '</p>']))