def linkToWithActiveTab(self, childItem, parentItem):
    return self.linkTo(parentItem.storeID) + '/' + self.toWebID(childItem)