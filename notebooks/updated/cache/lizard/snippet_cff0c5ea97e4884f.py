def open_as_pdf(self):
    report_urls_dict = report_urls(self.impact_function)
    for key, value in list(report_urls_dict.items()):
        report_urls_dict[key] = list(value.values())
    if self.dock:
        status = m.Message(m.Heading(self.dock.tr('Map Creator'), **
            INFO_STYLE), m.Paragraph(self.dock.tr(
            'Your PDF was created....opening using the default PDF viewer on your system.'
            )), m.ImportantText(self.dock.tr(
            'The generated pdfs were saved as:')))
        for path in report_urls_dict.get(pdf_product_tag['key'], []):
            status.add(m.Paragraph(path))
        status.add(m.Paragraph(m.ImportantText(self.dock.tr(
            'The generated htmls were saved as:'))))
        for path in report_urls_dict.get(html_product_tag['key'], []):
            status.add(m.Paragraph(path))
        status.add(m.Paragraph(m.ImportantText(self.dock.tr(
            'The generated qpts were saved as:'))))
        for path in report_urls_dict.get(qpt_product_tag['key'], []):
            status.add(m.Paragraph(path))
        send_static_message(self.dock, status)
    for path in report_urls_dict.get(pdf_product_tag['key'], []):
        QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(path))