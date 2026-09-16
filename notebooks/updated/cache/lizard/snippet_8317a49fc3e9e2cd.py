def get_last_response_xml(self, pretty_print_if_possible=False):
    response = None
    if self.__last_response is not None:
        if isinstance(self.__last_response, compat.str_type):
            response = self.__last_response
        else:
            response = tostring(self.__last_response, encoding='unicode',
                pretty_print=pretty_print_if_possible)
    return response