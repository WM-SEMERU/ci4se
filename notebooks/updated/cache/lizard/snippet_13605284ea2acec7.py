def solve(self):
    cycle = ['FR', 'RB', 'BL', 'LF']
    combine = self.combine()
    put = Formula(Step('y') * cycle.index(self.pair) or [])
    self.cube(put)
    self.pair = 'FR'
    estimated = self.estimated_position()
    for U_act in [Formula(), Formula('U'), Formula('U2'), Formula("U'")]:
        self.cube(U_act)
        for put_act in [Formula("R U R'"), Formula("R U' R'"), Formula(
            "R U2 R'"), Formula("F' U F"), Formula("F' U' F"), Formula(
            "F' U2 F")]:
            self.cube(put_act)
            if self.get_pair() == estimated:
                return combine + put + U_act + put_act
            self.cube(put_act.reverse())
        self.cube(U_act.reverse())