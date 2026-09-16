def versus_summaries(turns=2, sims_to_average=2, async_results_q=None):
    board, player, opponent, extra_actions = _state_investigator.get_versus()
    if extra_actions:
        extra_actions = 1
    if board is None:
        return tuple()
    averaged_summaries = list()
    advisors = list()
    for i in range(sims_to_average):
        advisor = versus.Advisor()
        advisor.reset(board, player, opponent, extra_actions)
        advisors.append(advisor)
    for turn in range(turns):
        summaries_by_action = dict()
        for i in range(sims_to_average):
            advisor = advisors[i]
            advisor.simulate_next_turn()
            for s in advisor.sorted_current_summaries():
                summaries_by_action.setdefault(s.action, list()).append(s)
        averaged_summaries = list()
        for action, summaries in summaries_by_action.items():
            board = summaries[0].board
            action = summaries[0].action
            score_sum = sum(s.score for s in summaries)
            score_avg = score_sum / len(summaries)
            manadrain_sum = sum(s.mana_drain_leaves for s in summaries)
            leaves_sum = sum(s.total_leaves for s in summaries)
            avg_summary = base.Summary(board, action, score_avg,
                manadrain_sum, leaves_sum)
            averaged_summaries.append(avg_summary)
        averaged_summaries.sort(key=lambda s: s.score, reverse=True)
        if not async_results_q is None:
            async_results_q.put(averaged_summaries)
    return averaged_summaries