def report_errors(audit, url):
    errors = AxeCoreAudit.get_errors(audit)
    if errors['total'] > 0:
        msg = "URL '{}' has {} errors:\n\n{}".format(url, errors['total'],
            AxeCoreAudit.format_errors(errors['errors']))
        raise AccessibilityError(msg)