def get_mock_personalization_dict():
    mock_pers = dict()
    mock_pers['to_list'] = [To('test1@example.com', 'Example User'), To(
        'test2@example.com', 'Example User')]
    mock_pers['cc_list'] = [To('test3@example.com', 'Example User'), To(
        'test4@example.com', 'Example User')]
    mock_pers['bcc_list'] = [To('test5@example.com'), To('test6@example.com')]
    mock_pers['subject'
        ] = 'Hello World from the Personalized SendGrid Python Library'
    mock_pers['headers'] = [Header('X-Test', 'test'), Header('X-Mock', 'true')]
    mock_pers['substitutions'] = [Substitution('%name%', 'Example User'),
        Substitution('%city%', 'Denver')]
    mock_pers['custom_args'] = [CustomArg('user_id', '343'), CustomArg(
        'type', 'marketing')]
    mock_pers['send_at'] = 1443636843
    return mock_pers