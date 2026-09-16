def append_overhead_costs(costs, new_id, overhead_percentage=0.15):
    total_time = 0
    for item in costs:
        total_time += item['time']
    costs.append({'id': new_id, 'task': 'Overhead, Bufixes & Iterations',
        'time': total_time * overhead_percentage})
    return costs