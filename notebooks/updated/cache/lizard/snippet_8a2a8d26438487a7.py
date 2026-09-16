def set_problem_result(result, problem_id):
    rdict = load_feedback()
    if not 'problems' in rdict:
        rdict['problems'] = {}
    cur_val = rdict['problems'].get(problem_id, '')
    rdict['problems'][problem_id] = [result, cur_val] if type(cur_val
        ) == str else [result, cur_val[1]]
    save_feedback(rdict)