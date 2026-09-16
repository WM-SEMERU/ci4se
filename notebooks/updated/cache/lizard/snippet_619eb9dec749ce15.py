def publish(self, ar):
    wf = api.get_tool('portal_workflow')
    status = wf.getInfoFor(ar, 'review_state')
    transitions = {'verified': 'publish', 'published': 'republish'}
    transition = transitions.get(status, 'prepublish')
    logger.info('AR Transition: {} -> {}'.format(status, transition))
    try:
        wf.doActionFor(ar, transition)
        return True
    except WorkflowException as e:
        logger.debug(e)
        return False