def format_with_handler(self, query_result, return_type):
    handler = self.get_handler(type(query_result), return_type)
    return handler.format_result(query_result)