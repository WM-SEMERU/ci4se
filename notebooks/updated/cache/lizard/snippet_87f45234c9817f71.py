def copy_keywords(self, shapefile_path):
    source_xml_path = resources_path('petabencana', 'flood-keywords.xml')
    output_xml_path = shapefile_path.replace('shp', 'xml')
    LOGGER.info('Copying xml to: %s' % output_xml_path)
    title_token = '[TITLE]'
    new_title = self.tr('Jakarta Floods - %s' % self.time_stamp)
    date_token = '[DATE]'
    new_date = self.time_stamp
    with open(source_xml_path) as source_file, open(output_xml_path, 'w'
        ) as output_file:
        for line in source_file:
            line = line.replace(date_token, new_date)
            line = line.replace(title_token, new_title)
            output_file.write(line)