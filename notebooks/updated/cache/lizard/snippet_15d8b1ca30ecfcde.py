def get_report(report=None):
    if not report:
        report = list_reports()[-1:][0]
    report_path = _get_reports_path(report)
    report_dict = {'report': report}
    for filename in os.listdir(report_path):
        with open(os.path.join(report_path, filename), 'r') as f:
            report_dict[filename] = f.read()
    return report_dict