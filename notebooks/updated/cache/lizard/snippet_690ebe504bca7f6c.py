def initialize(self):
    self.randomize()
    self.dweight = Numeric.zeros(self.size, 'f')
    self.delta = Numeric.zeros(self.size, 'f')
    self.wed = Numeric.zeros(self.size, 'f')
    self.wedLast = Numeric.zeros(self.size, 'f')
    self.target = Numeric.zeros(self.size, 'f')
    self.error = Numeric.zeros(self.size, 'f')
    self.activation = Numeric.zeros(self.size, 'f')
    self.netinput = Numeric.zeros(self.size, 'f')
    self.targetSet = 0
    self.activationSet = 0
    self.verify = 1
    self.pcorrect = 0
    self.ptotal = 0
    self.correct = 0
    self.minTarget = 0.0
    self.maxTarget = 1.0
    self.minActivation = 0.0
    self.maxActivation = 1.0