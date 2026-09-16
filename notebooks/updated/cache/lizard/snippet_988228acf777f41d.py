def hill_climbing(problem, iterations_limit=0, viewer=None):
    return _local_search(problem, _first_expander, iterations_limit=
        iterations_limit, fringe_size=1, stop_when_no_better=True, viewer=
        viewer)