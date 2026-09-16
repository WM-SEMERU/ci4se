def generate_budget_data_package(self, resource):
    if not self.are_budget_data_package_fields_filled_in(resource):
        return
    try:
        resource['schema'] = self.data.schema
    except exceptions.NotABudgetDataPackageException:
        log.debug('Resource is not a Budget Data Package')
        resource['schema'] = []
        return
    resource['BudgetDataPackage'] = True
    resource['standard'] = self.data.version
    resource['granularity'] = self.data.granularity
    resource['type'] = self.data.budget_type