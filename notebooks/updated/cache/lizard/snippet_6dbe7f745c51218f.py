def getIndexGrid(self, name):
    index_map = self.mapTableFile.indexMaps.filter_by(name=name).one()
    gssha_pro_card = self.getCard('#PROJECTION_FILE')
    if gssha_pro_card is None:
        raise ValueError('#PROJECTION_FILE card not found ...')
    with tmp_chdir(self.project_directory):
        return GDALGrid(index_map.filename, gssha_pro_card.value.strip('"')
            .strip("'"))