def compile(self):
    result = TEMPLATE
    for rule in self.rules:
        if rule[2]:
            arrow = '=>'
        else:
            arrow = '->'
        repr_rule = repr(rule[0] + arrow + rule[1])
        result += 'algo.add_rule({repr_rule})\n'.format(repr_rule=repr_rule)
    result += 'for line in stdin:\n'
    result += "    print(algo.execute(''.join(line.split())))"
    return result