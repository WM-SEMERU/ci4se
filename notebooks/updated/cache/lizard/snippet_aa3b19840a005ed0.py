def add_instance(self, instance):
    assert isinstance(instance, dict)
    item = defaults['common'].copy()
    item.update(defaults['instance'])
    item.update(instance['data'])
    item.update(instance)
    item['itemType'] = 'instance'
    item['isToggled'] = instance['data'].get('publish', True)
    item['hasCompatible'] = True
    item['category'] = item['category'] or item['family']
    self.add_section(item['category'])
    families = [instance['data']['family']]
    families.extend(instance['data'].get('families', []))
    item['familiesConcatenated'] += ', '.join(families)
    item = self.add_item(item)
    self.instances.append(item)