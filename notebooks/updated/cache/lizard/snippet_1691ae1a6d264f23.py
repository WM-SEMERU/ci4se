def get_largest_schedule_within_budget(self, budget, proportion_discard):
    valid_schedules_and_costs = []
    for R in range(1, budget):
        schedule = self.generate_hyperband_schedule(R, proportion_discard)
        cost = self.compute_schedule_cost(schedule)
        if cost <= budget:
            valid_schedules_and_costs.append((schedule, cost))
    valid_schedules_and_costs.sort(key=lambda x: x[1], reverse=True)
    return valid_schedules_and_costs[0][0]