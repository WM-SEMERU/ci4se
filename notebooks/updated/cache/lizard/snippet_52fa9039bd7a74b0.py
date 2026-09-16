def get_results():
    res = {}
    session = requests.Session()
    handle_url('http://www.gocomics.com/features', session, res)
    handle_url('http://www.gocomics.com/explore/espanol', session, res)
    handle_url('http://www.gocomics.com/explore/editorial_list', session, res)
    handle_url('http://www.gocomics.com/explore/sherpa_list', session, res)
    save_result(res, json_file)