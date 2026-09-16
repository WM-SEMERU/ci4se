def indicator_constraints(self, x):
    x = np.atleast_2d(x)
    I_x = np.ones((x.shape[0], 1))
    if self.constraints is not None:
        for d in self.constraints:
            try:
                exec('constraint = lambda x:' + d['constraint'], globals())
                ind_x = (constraint(x) <= 0) * 1
                I_x *= ind_x.reshape(x.shape[0], 1)
            except:
                print('Fail to compile the constraint: ' + str(d))
                raise
    return I_x