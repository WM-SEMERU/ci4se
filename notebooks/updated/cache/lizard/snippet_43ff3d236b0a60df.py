def execute_route(self, meta_data, request_pdu):
    try:
        function = create_function_from_request_pdu(request_pdu)
        results = function.execute(meta_data['unit_id'], self.route_map)
        try:
            return function.create_response_pdu(results)
        except TypeError:
            return function.create_response_pdu()
    except ModbusError as e:
        function_code = get_function_code_from_request_pdu(request_pdu)
        return pack_exception_pdu(function_code, e.error_code)
    except Exception as e:
        log.exception('Could not handle request: {0}.'.format(e))
        function_code = get_function_code_from_request_pdu(request_pdu)
        return pack_exception_pdu(function_code, ServerDeviceFailureError.
            error_code)