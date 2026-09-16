def first_parameter(self, singular_value):
    self.log('calc first term parameter @' + str(singular_value))
    first_term = self.I_minus_R(singular_value) * self.parcov * self.I_minus_R(
        singular_value)
    self.log('calc first term parameter @' + str(singular_value))
    return first_term