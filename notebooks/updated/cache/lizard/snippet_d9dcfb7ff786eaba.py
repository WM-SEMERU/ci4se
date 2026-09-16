def match_rules(tree, rules, fun=None, multi=False):
    if multi:
        context = match_rules_context_multi(tree, rules)
    else:
        context = match_rules_context(tree, rules)
        if not context:
            return None
    if fun:
        args = fun.__code__.co_varnames
        if multi:
            res = []
            for c in context:
                action_context = {}
                for arg in args:
                    if arg in c:
                        action_context[arg] = c[arg]
                res.append(fun(**action_context))
            return res
        else:
            action_context = {}
            for arg in args:
                if arg in context:
                    action_context[arg] = context[arg]
            return fun(**action_context)
    else:
        return context