def only_passed_and_wait(result):
    verdict = result.get('verdict', '').strip().lower()
    if verdict in Verdicts.PASS + Verdicts.WAIT:
        return result
    return None