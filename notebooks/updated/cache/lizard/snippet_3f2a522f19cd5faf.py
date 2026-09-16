def add_jira_status(test_key, test_status, test_comment):
    global attachments
    if test_key and enabled:
        if test_key in jira_tests_status:
            previous_status = jira_tests_status[test_key]
            test_status = 'Pass' if previous_status[1
                ] == 'Pass' and test_status == 'Pass' else 'Fail'
            if previous_status[2] and test_comment:
                test_comment = '{}\n{}'.format(previous_status[2], test_comment
                    )
            elif previous_status[2] and not test_comment:
                test_comment = previous_status[2]
            attachments += previous_status[3]
        jira_tests_status[test_key
            ] = test_key, test_status, test_comment, attachments