def solve(self, graph, timeout, debug=False, anim=None):
    savings_list = self.compute_savings_list(graph)
    solution = SavingsSolution(graph)
    start = time.time()
    for i, j in savings_list[:]:
        if solution.is_complete():
            break
        if solution.can_process((i, j)):
            solution, inserted = solution.process((i, j))
            if inserted:
                savings_list.remove((i, j))
                if anim:
                    solution.draw_network(anim)
        if time.time() - start > timeout:
            break
    return solution