def run(components=None, broker=None):
    components = components or COMPONENTS[GROUPS.single]
    components = _determine_components(components)
    broker = broker or Broker()
    for component in run_order(components):
        start = time.time()
        try:
            if (component not in broker and component in DELEGATES and
                is_enabled(component)):
                log.info('Trying %s' % get_name(component))
                result = DELEGATES[component].process(broker)
                broker[component] = result
        except MissingRequirements as mr:
            if log.isEnabledFor(logging.DEBUG):
                name = get_name(component)
                reqs = stringify_requirements(mr.requirements)
                log.debug('%s missing requirements %s' % (name, reqs))
            broker.add_exception(component, mr)
        except SkipComponent:
            pass
        except Exception as ex:
            tb = traceback.format_exc()
            log.warn(tb)
            broker.add_exception(component, ex, tb)
        finally:
            broker.exec_times[component] = time.time() - start
            broker.fire_observers(component)
    return broker