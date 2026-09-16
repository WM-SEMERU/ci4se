def add_interrupt_callback(gpio_id, callback, edge='both', pull_up_down=
    PUD_OFF, threaded_callback=False, debounce_timeout_ms=None):
    _rpio.add_interrupt_callback(gpio_id, callback, edge, pull_up_down,
        threaded_callback, debounce_timeout_ms)