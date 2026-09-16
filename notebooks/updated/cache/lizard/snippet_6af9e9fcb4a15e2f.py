def dump_report_content(self, request, result):
    output = StringIO()
    writer = csv.writer(output, **self.csv_kwargs)
    writer.writerows([result.headers] + result.values)
    return output.getvalue()