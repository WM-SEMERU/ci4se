def html(dom: str):
    r = _get_report()
    r.append_body(render.html(dom))
    r.stdout_interceptor.write_source('[ADDED] HTML\n')