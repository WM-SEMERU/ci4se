def find_case_control(items):
    cases = []
    controls = []
    for data in items:
        if population.get_affected_status(data) == 1:
            controls.append(data)
        else:
            cases.append(data)
    return cases, controls