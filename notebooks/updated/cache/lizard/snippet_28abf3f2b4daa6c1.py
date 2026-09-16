def update_helper_political_level(self):
    current_country = self.country_comboBox.currentText()
    index = self.admin_level_comboBox.currentIndex()
    current_level = self.admin_level_comboBox.itemData(index)
    content = None
    try:
        content = self.countries[current_country]['levels'][str(current_level)]
        if content == 'N/A' or content == 'fixme' or content == '':
            raise KeyError
    except KeyError:
        content = self.tr('undefined')
    finally:
        text = self.tr('which represents %s in') % content
        self.boundary_helper.setText(text)