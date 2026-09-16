def get_exposure(oqparam):
    exposure = asset.Exposure.read(oqparam.inputs['exposure'], oqparam.
        calculation_mode, oqparam.region, oqparam.ignore_missing_costs,
        by_country='country' in oqparam.aggregate_by)
    exposure.mesh, exposure.assets_by_site = exposure.get_mesh_assets_by_site()
    return exposure