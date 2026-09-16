def deliver_slice(schedule):
    if schedule.email_format == SliceEmailReportFormat.data:
        email = _get_slice_data(schedule)
    elif schedule.email_format == SliceEmailReportFormat.visualization:
        email = _get_slice_visualization(schedule)
    else:
        raise RuntimeError('Unknown email report format')
    subject = __('%(prefix)s %(title)s', prefix=config.get(
        'EMAIL_REPORTS_SUBJECT_PREFIX'), title=schedule.slice.slice_name)
    _deliver_email(schedule, subject, email)