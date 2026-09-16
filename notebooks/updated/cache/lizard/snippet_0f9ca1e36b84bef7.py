def calc_inc(self):
    system = self.system
    self.newton_call()
    A = sparse([[system.dae.Fx, system.dae.Gx], [system.dae.Fy, system.dae.Gy]]
        )
    inc = matrix([system.dae.f, system.dae.g])
    if system.dae.factorize:
        self.F = self.solver.symbolic(A)
        system.dae.factorize = False
    try:
        N = self.solver.numeric(A, self.F)
        self.solver.solve(A, self.F, N, inc)
    except ValueError:
        logger.warning('Unexpected symbolic factorization.')
        system.dae.factorize = True
    except ArithmeticError:
        logger.warning('Jacobian matrix is singular.')
        system.dae.check_diag(system.dae.Gy, 'unamey')
    return -inc