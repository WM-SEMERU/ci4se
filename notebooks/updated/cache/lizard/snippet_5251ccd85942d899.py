def _inject_dist(distname, kwargs={}, ns=locals()):
    dist_logp, dist_random, grad_logp = name_to_funcs(distname, ns)
    classname = capitalize(distname)
    ns[classname] = stochastic_from_dist(distname, dist_logp, dist_random,
        grad_logp, **kwargs)