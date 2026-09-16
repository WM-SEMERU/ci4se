def inverse(self):
    return OperatorComp(self.right.inverse, self.left.inverse, self.__tmp)