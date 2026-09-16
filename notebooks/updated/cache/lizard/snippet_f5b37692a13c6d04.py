def _update_resourcescenario(scenario, resource_scenario, dataset=None, new
    =False, user_id=None, source=None):
    if scenario is None:
        scenario = db.DBSession.query(Scenario).filter(Scenario.id == 1).one()
    ra_id = resource_scenario.resource_attr_id
    log.debug('Assigning resource attribute: %s', ra_id)
    try:
        r_scen_i = db.DBSession.query(ResourceScenario).filter(
            ResourceScenario.scenario_id == scenario.id, ResourceScenario.
            resource_attr_id == ra_id).one()
    except NoResultFound as e:
        log.info('Creating new RS')
        r_scen_i = ResourceScenario()
        r_scen_i.resource_attr_id = resource_scenario.resource_attr_id
        r_scen_i.scenario_id = scenario.id
        r_scen_i.scenario = scenario
        db.DBSession.add(r_scen_i)
    if scenario.locked == 'Y':
        log.info('Scenario %s is locked', scenario.id)
        return r_scen_i
    if dataset is not None:
        r_scen_i.dataset = dataset
        return r_scen_i
    dataset = resource_scenario.dataset
    value = dataset.parse_value()
    log.info('Assigning %s to resource attribute: %s', value, ra_id)
    if value is None:
        log.info('Cannot set data on resource attribute %s', ra_id)
        return None
    metadata = dataset.get_metadata_as_dict(source=source, user_id=user_id)
    data_unit_id = dataset.unit_id
    data_hash = dataset.get_hash(value, metadata)
    assign_value(r_scen_i, dataset.type.lower(), value, data_unit_id,
        dataset.name, metadata=metadata, data_hash=data_hash, user_id=
        user_id, source=source)
    return r_scen_i