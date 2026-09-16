def solve(ctx, length, height, silent, profile, **pieces):
    if not sum(pieces.values()):
        context = click.get_current_context()
        raise BadParameter('No piece provided.', ctx=context, param_hint=[
            '--{}'.format(label) for label in PIECE_LABELS])
    profiler = BProfile('solver-profile.png', enabled=profile)
    solver = SolverContext(length, height, **pieces)
    logger.info(repr(solver))
    logger.info('Searching positions...')
    with profiler:
        start = time.time()
        for result in solver.solve():
            if not silent:
                click.echo('{}'.format(result))
        processing_time = time.time() - start
    logger.info('{} results found in {:.2f} seconds.'.format(solver.
        result_counter, processing_time))
    if profile:
        logger.info('Execution profile saved at {}'.format(profiler.
            output_path))