def clip(layer_to_clip, mask_layer):
    output_layer_name = clip_steps['output_layer_name']
    output_layer_name = output_layer_name % layer_to_clip.keywords[
        'layer_purpose']
    parameters = {'INPUT': layer_to_clip, 'OVERLAY': mask_layer, 'OUTPUT':
        'memory:'}
    initialize_processing()
    feedback = create_processing_feedback()
    context = create_processing_context(feedback=feedback)
    result = processing.run('native:clip', parameters, context=context)
    if result is None:
        raise ProcessingInstallationError
    clipped = result['OUTPUT']
    clipped.setName(output_layer_name)
    clipped.keywords = layer_to_clip.keywords.copy()
    clipped.keywords['title'] = output_layer_name
    check_layer(clipped)
    return clipped