def add_rule_to_model(model, rule, annotations=None):
    try:
        model.add_component(rule)
        if annotations:
            model.annotations += annotations
    except ComponentDuplicateNameError:
        msg = 'Rule %s already in model! Skipping.' % rule.name
        logger.debug(msg)