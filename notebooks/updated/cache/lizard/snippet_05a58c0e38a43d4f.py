def get_other_answers_simple(pool, seeded_answers, get_student_item_dict,
    num_responses):
    ret = []
    pool = {int(k): v for k, v in pool.items()}
    total_in_pool = len(seeded_answers)
    merged_pool = convert_seeded_answers(seeded_answers)
    student_id = get_student_item_dict()['student_id']
    for key in pool:
        total_in_pool += len(pool[key])
        if student_id in pool[key].keys():
            total_in_pool -= 1
        if key in merged_pool:
            merged_pool[key].update(pool[key].items())
        else:
            merged_pool[key] = pool[key]
    selected = []
    while len(ret) < min(num_responses, total_in_pool):
        for option, students in merged_pool.items():
            student = student_id
            i = 0
            while (student == student_id or i > 100) and str(option
                ) + student not in selected:
                student = random.choice(students.keys())
                i += 1
            selected.append(str(option) + student)
            if student.startswith('seeded'):
                rationale = students[student]
            else:
                student_item = get_student_item_dict(student)
                submission = sas_api.get_answers_for_student(student_item)
                rationale = submission.get_rationale(0)
            ret.append({'option': option, 'rationale': rationale})
            if len(ret) >= min(num_responses, total_in_pool):
                break
    return {'answers': ret}