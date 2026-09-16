def _save_results(self):
    with open(self.results_file, 'w') as results_file:
        json.dump(self.results, results_file)