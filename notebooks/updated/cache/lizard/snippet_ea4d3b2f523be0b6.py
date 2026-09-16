def add_unique_runid(testcase, run_id=None):
    testcase['description'] = '{}<br id="{}"/>'.format(testcase.get(
        'description') or '', run_id or id(add_unique_runid))