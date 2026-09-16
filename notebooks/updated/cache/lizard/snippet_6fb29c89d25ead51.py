def volume_oscillator(volume, short_period, long_period):
    catch_errors.check_for_period_error(volume, short_period)
    catch_errors.check_for_period_error(volume, long_period)
    vo = 100 * ((sma(volume, short_period) - sma(volume, long_period)) /
        sma(volume, long_period))
    return vo