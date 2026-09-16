def get_review_history(brain_or_object, rev=True):
    obj = get_object(brain_or_object)
    review_history = []
    try:
        workflow = get_tool('portal_workflow')
        review_history = workflow.getInfoFor(obj, 'review_history')
    except WorkflowException as e:
        message = str(e)
        logger.error('Cannot retrieve review_history on {}: {}'.format(obj,
            message))
    if not isinstance(review_history, (list, tuple)):
        logger.error('get_review_history: expected list, recieved {}'.
            format(review_history))
        review_history = []
    if rev is True:
        review_history.reverse()
    return review_history