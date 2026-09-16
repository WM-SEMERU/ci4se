def init_drivers(enable_debug_driver=False):
    for driver in DRIVERS:
        try:
            if driver != DebugDriver or enable_debug_driver:
                CLASSES.append(driver)
        except Exception:
            continue