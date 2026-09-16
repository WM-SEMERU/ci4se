def sample(problem, N, num_levels=4, optimal_trajectories=None,
    local_optimization=True):
    if problem.get('groups'):
        sample = _sample_groups(problem, N, num_levels)
    else:
        sample = _sample_oat(problem, N, num_levels)
    if optimal_trajectories:
        sample = _compute_optimised_trajectories(problem, sample, N,
            optimal_trajectories, local_optimization)
    scale_samples(sample, problem['bounds'])
    return sample