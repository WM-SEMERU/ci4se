def get_asset_ids_by_repositories(self, repository_ids):
    id_list = []
    for asset in self.get_assets_by_repositories(repository_ids):
        id_list.append(asset.get_id())
    return IdList(id_list)