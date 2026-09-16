def to_dict(self):
    input_dict = super(StdPeriodic, self)._save_to_input_dict()
    input_dict['class'] = 'GPy.kern.StdPeriodic'
    input_dict['variance'] = self.variance.values.tolist()
    input_dict['period'] = self.period.values.tolist()
    input_dict['lengthscale'] = self.lengthscale.values.tolist()
    input_dict['ARD1'] = self.ARD1
    input_dict['ARD2'] = self.ARD2
    return input_dict