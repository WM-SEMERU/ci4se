def solve(self, solver=None, solverparameters=None):
    if self.F is None:
        raise Exception(
            "Relaxation is not generated yet. Call 'SdpRelaxation.get_relaxation' first"
            )
    solve_sdp(self, solver, solverparameters)