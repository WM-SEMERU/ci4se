def process_response(self, result):
    if len(result) == 3:
        data = result[0]
        headers = result[2]
        if self.HEADER_API_VERSION in headers:
            api_version = headers[self.HEADER_API_VERSION]
            if (not self.already_printed_version_warning and not self.
                is_up_to_date(api_version)):
                print(
                    "Warning: Looks like you're using an outdated API Version, please consider updating (server "
                     + api_version + ' / client ' + self.__version__ + ')')
                self.already_printed_version_warning = True
        return data
    return result