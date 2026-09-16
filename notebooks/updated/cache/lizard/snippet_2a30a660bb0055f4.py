def on_log(request, page_name):
    page = Page.query.filter_by(name=page_name).first()
    if page is None:
        return page_missing(request, page_name, False)
    return Response(generate_template('action_log.html', page=page))