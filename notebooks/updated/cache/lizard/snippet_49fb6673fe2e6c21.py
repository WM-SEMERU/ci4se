def evaluator(evaluate):

    @functools.wraps(evaluate)
    def inspyred_evaluator(candidates, args):
        fitness = []
        for candidate in candidates:
            fitness.append(evaluate(candidate, args))
        return fitness
    inspyred_evaluator.single_evaluation = evaluate
    return inspyred_evaluator