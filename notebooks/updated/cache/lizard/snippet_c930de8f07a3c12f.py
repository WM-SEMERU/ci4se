def _matches_billing(price, hourly):
    return any([hourly and price.get('hourlyRecurringFee') is not None, not
        hourly and price.get('recurringFee') is not None])