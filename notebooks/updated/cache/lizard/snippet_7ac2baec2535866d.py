def parse_rule(name, rule_text, do_raise=False):
    try:
        return rule.parseString(rule_text, parseAll=True)[0]
    except pyparsing.ParseException as exc:
        if do_raise:
            raise
        log = logging.getLogger('policies')
        log.warn('Failed to parse rule %r: %s' % (name, exc))
        log.warn('Rule line: %s' % exc.line)
        log.warn('Location : %s^' % (' ' * (exc.col - 1)))
        return Instructions([Constant(False), set_authz])