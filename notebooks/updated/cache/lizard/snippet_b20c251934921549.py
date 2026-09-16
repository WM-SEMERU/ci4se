def generate_128bit_trace_id(self):
    if 'generate_128bit_trace_id' in self.config:
        return get_boolean(self.config['generate_128bit_trace_id'], False)
    return os.getenv('JAEGER_TRACEID_128BIT') == 'true'