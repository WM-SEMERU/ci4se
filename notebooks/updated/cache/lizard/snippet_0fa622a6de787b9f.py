def iterate_storyline(ctx):
    logger.debug('# start iterate')
    compiled_story = ctx.compiled_story()
    if not compiled_story:
        return
    for step in range(ctx.current_step(), len(compiled_story.story_line)):
        ctx = ctx.clone()
        tail = ctx.stack_tail()
        ctx.message = modify_stack_in_message(ctx.message, lambda stack: 
            stack[:-1] + [{'data': tail['data'], 'step': step, 'topic':
            tail['topic']}])
        logger.debug('# [{}] iterate'.format(step))
        logger.debug(ctx)
        ctx = yield ctx