def collect_results(results_file):
    with open(results_file, 'r') as results:
        data = json.load(results)
    return data