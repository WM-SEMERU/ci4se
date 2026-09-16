def horn_sat(formula):
    CLAUSES = range(len(formula))
    score = [(0) for c in CLAUSES]
    posvar_in_clause = [None for c in CLAUSES]
    clauses_with_negvar = defaultdict(set)
    for c in CLAUSES:
        posvar, negvars = formula[c]
        score[c] = len(set(negvars))
        posvar_in_clause[c] = posvar
        for v in negvars:
            clauses_with_negvar[v].add(c)
    pool = [set() for s in range(max(score) + 1)]
    for c in CLAUSES:
        pool[score[c]].add(c)
    solution = set()
    while pool[0]:
        curr = pool[0].pop()
        v = posvar_in_clause[curr]
        if v == None:
            return None
        if v in solution or curr in clauses_with_negvar[v]:
            continue
        solution.add(v)
        for c in clauses_with_negvar[v]:
            pool[score[c]].remove(c)
            score[c] -= 1
            pool[score[c]].add(c)
    return solution