def DownloadPqlResultToCsv(self, pql_query, file_handle, values=None):
    pql_writer = csv.writer(file_handle, delimiter=',', quotechar='"',
        quoting=csv.QUOTE_ALL)
    self._PageThroughPqlSet(pql_query, pql_writer.writerow, values)