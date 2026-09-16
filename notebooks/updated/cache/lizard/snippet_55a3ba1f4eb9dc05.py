def get_endpoints(self):

    def process_result(result):
        return [line.split(';')[0][2:-1] for line in result.split(',')]
    return Command('get', ['.well-known', 'core'], parse_json=False,
        process_result=process_result)