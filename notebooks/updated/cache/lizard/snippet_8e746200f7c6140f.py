def XML_save_parsed_data_to_csv(self, output_filename='output.csv'):
    result = self.XML_parse_rectlabel_app_output()
    ff = open(output_filename, 'w', encoding='utf8')
    for line in result:
        ff.write(line + '\n')
    ff.close()