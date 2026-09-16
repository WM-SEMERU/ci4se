def BC_Periodic(self):
    if self.BC_E == 'Periodic' and self.BC_W == 'Periodic':
        pass
    else:
        sys.exit(
            'Having the boundary opposite a periodic boundary condition\n' +
            """be fixed and not include an implicit periodic boundary
""" +
            'condition makes no physical sense.\n' +
            'Please fix the input boundary conditions. Aborting.')
    self.diags = np.vstack((self.r1, self.r2, self.l2, self.l1, self.c0,
        self.r1, self.r2, self.l2, self.l1))
    self.offsets = np.array([1 - self.ncolsx, 2 - self.ncolsx, -2, -1, 0, 1,
        2, self.ncolsx - 2, self.ncolsx - 1])