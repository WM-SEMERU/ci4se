def get_logits_over_interval(*args, **kwargs):
    warnings.warn(
        '`get_logits_over_interval` has moved to `cleverhans.plot.pyplot_image`. cleverhans.utils.get_logits_over_interval may be removed on or after 2019-04-24.'
        )
    from cleverhans.plot.pyplot_image import get_logits_over_interval as new_get_logits_over_interval
    return new_get_logits_over_interval(*args, **kwargs)