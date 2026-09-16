def save_report_to_html(self):
    html = self.page().mainFrame().toHtml()
    if self.report_path is not None:
        html_to_file(html, self.report_path)
    else:
        msg = self.tr('report_path is not set')
        raise InvalidParameterError(msg)