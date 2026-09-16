def condor_submit(submit_file):
    external_id = None
    try:
        submit = Popen(('condor_submit', submit_file), stdout=PIPE, stderr=
            STDOUT)
        message, _ = submit.communicate()
        if submit.returncode == 0:
            external_id = parse_external_id(message, type='condor')
        else:
            message = PROBLEM_PARSING_EXTERNAL_ID
    except Exception as e:
        message = str(e)
    return external_id, message