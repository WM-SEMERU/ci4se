def determine_result(self, returncode, returnsignal, output, isTimeout):
    for line in output:
        if line.startswith('KLEE: ERROR: '):
            if line.find('ASSERTION FAIL:') != -1:
                return result.RESULT_FALSE_REACH
            elif line.find('memory error: out of bound pointer') != -1:
                return result.RESULT_FALSE_DEREF
            elif line.find('overflow') != -1:
                return result.RESULT_FALSE_OVERFLOW
            else:
                return 'ERROR ({0})'.format(returncode)
        if line.startswith('KLEE: done'):
            return result.RESULT_DONE
    return result.RESULT_UNKNOWN