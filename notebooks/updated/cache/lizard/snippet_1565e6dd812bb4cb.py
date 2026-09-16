def _get_group_dataframes(self):
    if isinstance(self.data, GroupedDataFrame):
        grouper = self.data.groupby()
        return (gdf for _, gdf in grouper if not gdf.empty)
    else:
        return self.data,