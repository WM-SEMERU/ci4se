def assignParameters(self, solution_next, IncomeDstn, LivPrb, DiscFac, CRRA,
    Rfree, PermGroFac, BoroCnstArt, aXtraGrid, vFuncBool, CubicBool):
    ConsPerfForesightSolver.assignParameters(self, solution_next, DiscFac,
        LivPrb, CRRA, Rfree, PermGroFac)
    self.BoroCnstArt = BoroCnstArt
    self.IncomeDstn = IncomeDstn
    self.aXtraGrid = aXtraGrid
    self.vFuncBool = vFuncBool
    self.CubicBool = CubicBool