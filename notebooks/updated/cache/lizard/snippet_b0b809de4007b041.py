def create_detailed_results(result):
    string = ''
    string += 'STATUS: {}\n'.format(result['status'])
    if result['feedback']:
        string += 'WARNINGS: {}\n'.format(len(result['feedback']['wrnMsgs']))
        for msg in result['feedback']['wrnMsgs']:
            string += '- {}\n'.format(msg)
        string += 'ERRORS: {}\n'.format(len(result['feedback']['errMsgs']))
        for msg in result['feedback']['errMsgs']:
            string += '- {}\n'.format(msg)
    return string