def get_items(self, scenario_id):
    items = get_session().query(ResourceGroupItem).filter(ResourceGroupItem
        .group_id == self.id).filter(ResourceGroupItem.scenario_id ==
        scenario_id).all()
    return items