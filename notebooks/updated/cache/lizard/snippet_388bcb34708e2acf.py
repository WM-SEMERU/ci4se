def _fetch_with_touchdowns(self, dialog, segment_factory, *args, **kwargs):
    responses = []
    touchdown_counter = 1
    touchdown = None
    while touchdown or touchdown_counter == 1:
        seg = segment_factory(touchdown)
        rm = dialog.send(seg)
        for resp in rm.response_segments(seg, *args, **kwargs):
            responses.append(resp)
        touchdown = None
        for response in rm.responses(seg, '3040'):
            touchdown = response.parameters[0]
            break
        if touchdown:
            logger.info('Fetching more results ({})...'.format(
                touchdown_counter))
        touchdown_counter += 1
    return responses