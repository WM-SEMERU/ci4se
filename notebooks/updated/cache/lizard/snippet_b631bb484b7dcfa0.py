def system_multicall(self, call_list):
    results = []
    for call in call_list:
        method_name = call['methodName']
        params = call['params']
        try:
            results.append([self._dispatch(method_name, params)])
        except Fault as fault:
            results.append({'faultCode': fault.faultCode, 'faultString':
                fault.faultString})
        except:
            exc_type, exc_value, exc_tb = sys.exc_info()
            results.append({'faultCode': 1, 'faultString': '%s:%s' % (
                exc_type, exc_value)})
    return results