def vel_grad_avg(self):
    return (u.standard_gravity * self.HL / (pc.viscosity_kinematic(self.
        temp) * self.Gt)).to(u.s ** -1)