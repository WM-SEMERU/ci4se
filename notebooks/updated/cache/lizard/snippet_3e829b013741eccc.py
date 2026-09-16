def determine_result(self, returncode, returnsignal, output, isTimeout):
    if not output:
        return 'ERROR - no output'
    last = output[-1]
    if isTimeout:
        return 'TIMEOUT'
    if returncode != 0:
        return 'ERROR - Pre-run'
    if last is None:
        return 'ERROR - no output'
    elif 'result: true' in last:
        return result.RESULT_TRUE_PROP
    elif 'result: false' in last:
        return result.RESULT_FALSE_REACH
    else:
        return result.RESULT_UNKNOWN