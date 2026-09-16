def filter_model_items(index_instance, model_items, model_name, start_date,
    end_date):
    if index_instance.updated_field is None:
        logger.warning(
            'No updated date field found for {} - not restricting with start and end date'
            .format(model_name))
    else:
        if start_date:
            model_items = model_items.filter(**{'{}__gte'.format(
                index_instance.updated_field): __str_to_tzdate__(start_date)})
        if end_date:
            model_items = model_items.filter(**{'{}__lte'.format(
                index_instance.updated_field): __str_to_tzdate__(end_date)})
    return model_items