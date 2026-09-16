def head(source, count: int=5):
    r = _get_report()
    r.append_body(render_texts.head(source, count=count))
    r.stdout_interceptor.write_source('[ADDED] Head\n')