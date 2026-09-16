def delete(block_id):
    _url = get_root_url()
    try:
        DB.delete_processing_block(block_id)
        response = dict(message='Deleted block', id='{}'.format(block_id),
            links=dict(list='{}/processing-blocks'.format(_url), home='{}'.
            format(_url)))
        return response, HTTPStatus.OK
    except RuntimeError as error:
        response = dict(error='Failed to delete Processing Block: {}'.
            format(block_id), reason=str(error), links=dict(list=
            '{}/processing-blocks'.format(_url), home='{}'.format(_url)))
        return response, HTTPStatus.OK