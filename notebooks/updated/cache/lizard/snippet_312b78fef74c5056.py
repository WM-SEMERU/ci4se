def _at_if(self, calculator, rule, scope, block):
    if block.directive != '@if':
        if '@if' not in rule.options:
            raise SyntaxError('@else with no @if (%s)' % (rule.file_and_line,))
        if rule.options['@if']:
            return
    condition = calculator.calculate(block.argument)
    if condition:
        inner_rule = rule.copy()
        inner_rule.unparsed_contents = block.unparsed_contents
        if not self.should_scope_loop_in_rule(inner_rule):
            inner_rule.namespace = rule.namespace
        self.manage_children(inner_rule, scope)
    rule.options['@if'] = condition