def create(self, price_estimate):
    kwargs = {}
    try:
        previous_price_estimate = price_estimate.get_previous()
    except ObjectDoesNotExist:
        pass
    else:
        configuration = (previous_price_estimate.consumption_details.
            configuration)
        kwargs['configuration'] = configuration
    month_start = core_utils.month_start(datetime.date(price_estimate.year,
        price_estimate.month, 1))
    kwargs['last_update_time'] = month_start
    return super(ConsumptionDetailsQuerySet, self).create(price_estimate=
        price_estimate, **kwargs)