def handle_error(self, error, download_request):
    if hasattr(error, 'errno') and error.errno == errno.EACCES:
        self.handle_certificate_problem(str(error))
    else:
        self.handle_general_download_error(str(error), download_request)