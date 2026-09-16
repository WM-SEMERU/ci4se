def arrival_delay_greater_than(item_id, delay, namespace='_expected_arrival'):
    expected = get_state(item_id, namespace=namespace)
    now = time.time()
    if expected and now - expected > delay:
        logger.error('Timeout: waited %s seconds for parent.', delay)
        return True
    elif expected:
        logger.info('Still out of order but no timeout: %s-%s <= %s.', now,
            expected, delay)
        return False
    elif delay > 0:
        logger.info("Storing expected arrival time (%s) for context '%s'",
            datetime.fromtimestamp(now).isoformat(), item_id)
        set_state(item_id, now, namespace=namespace)
        return False
    else:
        logger.info('Event is out of order but not waiting for parent.')
        return True