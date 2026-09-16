def report(title='Unhandled Exception', exec_info=(), **kwargs):
    exc_type, exc_value, tb = exec_info or sys.exc_info()
    reporter = ExceptionReporter(exc_type, exc_value, tb)
    html = reporter.get_traceback_html(**kwargs)
    mail_admins(title, 'html only', html_message=html)