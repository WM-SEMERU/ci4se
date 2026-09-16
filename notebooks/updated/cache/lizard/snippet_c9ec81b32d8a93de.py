def get_max_bond_distance(self, el1_sym, el2_sym):
    return sqrt((self.el_radius[el1_sym] + self.el_radius[el2_sym] + self.
        tol) ** 2)