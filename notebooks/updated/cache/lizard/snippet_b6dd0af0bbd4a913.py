def _check_spot_bid(spot_bid, spot_history):
    average = mean([datum.price for datum in spot_history])
    if spot_bid > average * 2:
        logger.warn(
            "Your bid $ %f is more than double this instance type's average spot price ($ %f) over the last week"
            , spot_bid, average)