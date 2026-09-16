def _get_upgrade_prices(self, instance_id, include_downgrade_options=True):
    mask = ['id', 'locationGroupId', 'categories[name,id,categoryCode]',
        'item[description,capacity,units]']
    mask = 'mask[%s]' % ','.join(mask)
    return self.guest.getUpgradeItemPrices(include_downgrade_options, id=
        instance_id, mask=mask)