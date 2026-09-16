def get_aws_index(self):
    if self.aws_index is not None:
        return self.aws_index
    tile_info_list = get_tile_info(self.tile_name, self.datetime, all_tiles
        =True)
    if not tile_info_list:
        raise ValueError('Cannot find aws_index for specified tile and time')
    if self.data_source is DataSource.SENTINEL2_L2A:
        for tile_info in sorted(tile_info_list, key=self._parse_aws_index):
            try:
                self.aws_index = self._parse_aws_index(tile_info)
                self.get_tile_info()
                return self.aws_index
            except AwsDownloadFailedException:
                pass
    return self._parse_aws_index(tile_info_list[0])