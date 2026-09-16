def _at_print(self, calculator, rule, scope, block):
    value = calculator.calculate(block.argument)
    sys.stderr.write('%s\n' % value)