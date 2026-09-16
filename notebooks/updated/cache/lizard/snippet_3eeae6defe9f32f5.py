def get_service_info(self, obj):
    info = self.get_base_info(obj)
    info.update({'short_title': obj.getShortTitle(), 'scientific_name': obj
        .getScientificName(), 'unit': obj.getUnit(), 'keyword': obj.
        getKeyword(), 'methods': map(self.get_method_info, obj.getMethods()
        ), 'calculation': self.get_calculation_info(obj.getCalculation()),
        'price': obj.getPrice(), 'currency_symbol': self.get_currency().
        symbol, 'accredited': obj.getAccredited(), 'category': obj.
        getCategoryTitle(), 'poc': obj.getPointOfCapture()})
    dependencies = get_calculation_dependencies_for(obj).values()
    info['dependencies'] = map(self.get_base_info, dependencies)
    return info